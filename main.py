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

#3fa85f64-5717-4562-b3fc-2c963f66afa6

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
def get_business(id: UUID, db: Session = Depends(get_db)):
    business = db.query(models.Business).filter(models.Business.id == id).first()
    if business is None:
        raise HTTPException(status_code=404, detail="Business not found")
    return business

def get_business(id: UUID):
    return businesses_db[id]
    
    # tu turno: buscá en businesses_db usando ese id y devolvelo


@app.post("/businesses/{id}/diagnose")
def diagnose_business(id: UUID, data: DiagnosisRequest, db: Session = Depends(get_db)):
    business = db.query(models.Business).filter(models.Business.id == id).first()
    if business is None:
            raise HTTPException(status_code=404, detail="Business not found")
    detectors = create_detectors(data)
    session = DiagxSession(detectors)
    result = session.run_diagnosis()

    db_diagnostic = models.Diagnostic(business_id= id, issues= result)
    db.add(db_diagnostic)
    db.commit()
    db.refresh(db_diagnostic)

    return {"diagnostic_id": db_diagnostic.id, "issues": result}

@app.get("/businesses/{id}/diagnostics")
def get_diagnostics_history(id: UUID, db: Session = Depends(get_db)):
      business = db.query(models.Business).filter(models.Business.id == id).first()
      if business is None:
            raise HTTPException(status_code=404, detail="Business not found")
    
      return db.query(models.Diagnostic).filter(models.Diagnostic.business_id == id).all()
  
