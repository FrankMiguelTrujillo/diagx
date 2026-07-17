# -*- coding: utf-8 -*-

from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List, Protocol
from datetime import datetime
from uuid import UUID, uuid4




ronaldo = LowSalesDetail(monthly_revenue = 1000,
                       target_revenue = 1100,
                       revenue_growth_rate = -0.10,
                       average_ticket_value = 100,
                       churn_rate = 0.7)

class GetLowSales:
  def __init__(self, LowSalesDetail):
    self.issues = LowSalesDetail

  def detect_issues(self):
    issue = []
    if self.issues.monthly_revenue < self.issues.target_revenue:
      issue.append(f"Less expected revenue")

    if self.issues.revenue_growth_rate < 0:
      issue.append(f"Decrement in revenue")

    if self.issues.average_ticket_value > 100:
      issue.append(f"Expensive ticket value")

    if self.issues.churn_rate > 0.2:
      issue.append(f"Low retention rate")
    return issue

class LowTrafficDetail(BaseModel):
    total_visitors: int
    conversion_rate: float
    customer_acquisition_cost: float
    primary_acquisition_channel: str = Field(..., example="Social Media")
    bounce_rate: Optional[float] = None

class GetLowTraffic:
     def __init__(self, LowTrafficDetail):
      self.issuestraffic = LowTrafficDetail

     def detect_issues(self):
      issuetraffic = []
      if self.issuestraffic.conversion_rate < 0.3:
        issuetraffic.append(f"Less expected conversion rate")

      if self.issuestraffic.customer_acquisition_cost > 100:
        issuetraffic.append(f"Expensive customer acquisition cost")

      if self.issuestraffic.bounce_rate is not None and self.issuestraffic.bounce_rate > 0.6:
        issuetraffic.append(f"Big bounce rate")

      if self.issuestraffic.total_visitors < 10:
        issuetraffic.append(f"Low visitors rate")
      return issuetraffic

messi = LowTrafficDetail(total_visitors = 100,
                         conversion_rate = 0.4,
                         customer_acquisition_cost = 110,
                         primary_acquisition_channel = "Social Media",
                         bounce_rate = 0.7)
 
 
class BadReputationDetail(BaseModel):
    net_promoter_score: int = Field(ge=-100, le=100)
    percentage_negative_reviews: float
    refund_request_rate: float
    sentiment_index: float = Field(description="AI-generated score from 0.0 to 1.0")
    main_complaint_theme: str = Field(..., example="Slow delivery")
    
class GetBadReputation:
     def __init__(self, BadReputationDetail):
      self.issuesreputation = BadReputationDetail

     def detect_issues(self):
      issuesreputation = []
      if self.issuesreputation.net_promoter_score < 0:
        issuesreputation.append(f"Disappointed net promoter score")

      if self.issuesreputation.percentage_negative_reviews > 0.4:
        issuesreputation.append(f"Worrying percentage of negative reviews")

      if self.issuesreputation.refund_request_rate > 0.4:
        issuesreputation.append(f"Worrying refund request rate")

      if self.issuesreputation.sentiment_index < 0.6:
        issuesreputation.append(f"Worrying sentiment index")
      return issuesreputation

neymar = BadReputationDetail(net_promoter_score = -1,
                         percentage_negative_reviews = 0.45,
                         refund_request_rate = 0.6,
                         sentiment_index = 0.4,
                         main_complaint_theme = "slow delivery")

class ManagementDetail(BaseModel):
    fixed_operational_costs: float
    variable_costs: float
    all_earning: float
    inventory_turnover: float
    automation_score: float = Field(ge=0, le=1) # 0 to 1 scale
    administrative_waste_estimate: float
    
class GetManagement:
     def __init__(self, ManagementDetail):
      self.issuesmanagement = ManagementDetail

     def detect_issues(self):
      issuesmanagement = []
      if self.issuesmanagement.fixed_operational_costs + self.issuesmanagement.variable_costs > self.issuesmanagement.all_earning:
        issuesmanagement.append(f"Negative inventory balance")

      if self.issuesmanagement.inventory_turnover < 0:
        issuesmanagement.append(f"Negative inventory turn over")

      if self.issuesmanagement.automation_score < 0.4:
        issuesmanagement.append(f"Worrying automation_score")
        
      return issuesmanagement
    
suarez = ManagementDetail(fixed_operational_costs = 1000,
                         variable_costs = 600,
                         all_earning = 1500,
                         inventory_turnover = -100,
                         automation_score = 0.3,
                         administrative_waste_estimate = 0)

class BrokenDetector:
    def check_problems(self):  # nombre mal escrito, no es detect_issues
        return ["algo"]
        
class IssueDetector(Protocol):
    def detect_issues(self) -> list:
        ...
        
class DiagxSession:
    def __init__(self, detectors: list[IssueDetector]):
        self.detectors = detectors

    def run_diagnosis(self) -> list[str]:
        all_issues = []
        for detector in self.detectors:
            all_issues.extend(detector.detect_issues())
        return all_issues

session = DiagxSession([
    GetLowSales(ronaldo),
    GetLowTraffic(messi),
    GetManagement(suarez),
    GetBadReputation(neymar),
    
    # el día que agregues un quinto, solo sumás una línea acá
])

resultado = session.run_diagnosis()
print(resultado)

class BusinessData(BaseModel):
    LowSalesDetail: LowSalesDetail
    LowTrafficDetail: LowTrafficDetail
    ManagementDetail: ManagementDetail
    BadReputationDetail: BadReputationDetail

data_de_prueba = BusinessData(
    LowSalesDetail=ronaldo,      # tu instancia de LowSalesDetail (¿tenías alguna ya creada?)
    LowTrafficDetail=messi,    # tu instancia de traffic
    ManagementDetail=suarez,
    BadReputationDetail=neymar
)

def create_detectors(data) -> list[IssueDetector]:
    return [GetLowSales(data.LowSalesDetail), GetLowTraffic(data.LowTrafficDetail),GetManagement(data.ManagementDetail), GetBadReputation(data.BadReputationDetail)]

detectores = create_detectors(data_de_prueba)

# ¿Devolvió 4 elementos, ni más ni menos?
assert len(detectores) == 4

# ¿Cada elemento realmente tiene detect_issues()?
for d in detectores:
    assert hasattr(d, "detect_issues")
session = DiagxSession(create_detectors(data_de_prueba))
resultado = session.run_diagnosis()
print(resultado)