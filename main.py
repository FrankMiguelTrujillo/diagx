from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from metodos_solid import create_detectors
from metodos_solid import DiagxSession
from metodos_solid import LowSalesDetail
from metodos_solid import LowTrafficDetail
from metodos_solid import ManagementDetail
from metodos_solid import BadReputationDetail

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
def create_business(business: BusinessBasic):
    businesses_db[business.id] = business
    return business

@app.get("/businesses/{id}")
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

    diagnostics_db[id] = diagnostics_db.get(id, []) + [result]

    return {"business_id": id, "issues": result}