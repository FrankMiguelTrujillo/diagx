from pydantic import BaseModel, Field
from typing import Optional
from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
from database import Base

class Business(Base):
    __tablename__ = "businesses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    sector = Column(String, nullable=False)
    monthly_revenue = Column(Float, nullable=False)

    diagnostics = relationship("Diagnostic", back_populates="business")


class Diagnostic(Base):
    __tablename__ = "diagnostics"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    business_id = Column(UUID(as_uuid=True), ForeignKey("businesses.id"), nullable=False)
    timestamp = Column(DateTime, default=datetime.now)
    issues = Column(JSON, nullable=False)

    business = relationship("Business", back_populates="diagnostics")
# =====================================================================
# 1. THE SCHEMAS (Previously models.py)
# =====================================================================
class BusinessMetrics(BaseModel):
    company_name: str = Field(..., example="Acme Carpentry")
    industry: str = Field(..., example="Manufacturing")
    monthly_revenue: float = Field(..., gt=0, description="Monthly revenue in USD or COP")
    operational_costs: float = Field(..., ge=0)
    employee_count: int = Field(..., gt=0)
    sector_category_tic: Optional[bool] = Field(default=False, description="Uses advanced technology/TIC tools")

class DiagnosticResponse(BaseModel):
    status: str
    efficiency_score: float
    primary_bottleneck: str
    recommended_action: str

# =====================================================================
# 2. THE ENGINE (Previously engine.py)
# =====================================================================
def calculate_diagnostic(metrics: BusinessMetrics) -> DiagnosticResponse:
    if metrics.monthly_revenue <= 0:
        return DiagnosticResponse(
            status="Error",
            efficiency_score=0.0,
            primary_bottleneck="Invalid Revenue Data",
            recommended_action="Ensure monthly revenue is greater than zero."
        )

    margin = (metrics.monthly_revenue - metrics.operational_costs) / metrics.monthly_revenue
    rev_per_employee = metrics.monthly_revenue / metrics.employee_count
    benchmark_rev = 2000.0

    productivity_score = min(rev_per_employee / benchmark_rev, 1.0)

    if metrics.sector_category_tic:
        productivity_score = min(productivity_score * 1.15, 1.0)

    margin_score = max(margin, 0.0)
    efficiency_score = ((margin_score * 0.6) + (productivity_score * 0.4)) * 100

    if margin < 0.15:
        bottleneck = "High Operational Overhead"
        action = "Analyze fixed costs and optimize raw material procurement or resource allocation."
    elif rev_per_employee < (benchmark_rev * 0.5):
        bottleneck = "Low Labor Productivity"
        action = "Implement standard operating procedures (SOPs) or introduce automation tools."
    else:
        bottleneck = "Scalability Restrictions"
        action = "Focus on client acquisition pipelines and expanding market share."

    status = "Healthy" if efficiency_score >= 70 else "Critical"

    return DiagnosticResponse(
        status=status,
        efficiency_score=round(efficiency_score, 2),
        primary_bottleneck=bottleneck,
        recommended_action=action
    )

print("Schemas and Engine successfully loaded into memory!")

pr = BusinessMetrics(
    company_name="Acme Carpentry",
    industry="Manufacturing",
    monthly_revenue=2000.0,
    operational_costs=1000.0,
    employee_count=55,
    sector_category_tic=False
)