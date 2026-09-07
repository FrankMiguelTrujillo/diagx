from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from metodos_solid import create_detectors
from metodos_solid import DiagxSession
from metodos_solid import LowSalesDetail
from metodos_solid import LowTrafficDetail
from metodos_solid import ManagementDetail
from metodos_solid import BadReputationDetail
from datetime import datetime
from sqlalchemy.orm import Session
from database import SessionLocal
import models

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()
businesses_db = {}
diagnostics_db = {}

class DiagnosisRequest(BaseModel):
    sales: LowSalesDetail
    traffic: LowTrafficDetail
    management: ManagementDetail
    reputation: BadReputationDetail
    
class BusinessBasic(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    sector: str
    monthly_revenue: float
    # podés ir agregando el resto de campos que ya tenías en tus otras sesiones

@app.get("/")
def root():
    return {"status": "Diagx API running"}

@app.post("/businesses")
def create_business(business: BusinessBasic, db: Session = Depends(get_db)):
    db_business = models.Business(
        name=business.name,
        sector=business.sector,
        monthly_revenue=business.monthly_revenue
    )
    db.add(db_business)
    db.commit()
    db.refresh(db_business)
    return db_business
@app.get("/businesses/{id}")
def get_business(id: UUID):
    if id not in businesses_db:
        raise HTTPException(status_code=404, detail="Business not found")
    return businesses_db[id]

def get_business(id: UUID):
    return businesses_db[id]
    
    # tu turno: buscá en businesses_db usando ese id y devolvelo


@app.post("/businesses/{id}/diagnose")
def diagnose_business(id: UUID, data: DiagnosisRequest):
    if id not in businesses_db:
        raise HTTPException(status_code=404, detail="Business not found")

    detectors = create_detectors(data)
    session = DiagxSession(detectors)
    result = session.run_diagnosis()

    entry = {"timestamp": datetime.now().isoformat(), "issues": result}
    diagnostics_db[id] = diagnostics_db.get(id, []) + [entry]

    return {"business_id": id, "issues": result}

@app.get("/businesses/{id}/diagnostics")
def get_diagnostics_history(id: UUID):
      if id not in businesses_db:
        raise HTTPException(status_code=404, detail="Business not found")
    
      return diagnostics_db.get(id, []) 
  
