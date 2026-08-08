from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_business_with_valid_data():
    response = client.post("/businesses", json={
        "name": "Gómez Carpentry",
        "sector": "Manufacturing",
        "monthly_revenue": 5000
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Gómez Carpentry"

    # tu turno: agregá un assert más, verificando algo del contenido de la respuesta
def test_create_business_missing_name():
    response = client.post("/businesses", json={
        "sector": "Manufacturing",
        "monthly_revenue": 5000
        # fijate que "name" no está
    })
    assert response.status_code == 422
    
def test_get_business_not_found():
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = client.get(f"/businesses/{fake_id}")
    assert response.status_code == 404
def test_diagnose_business():
    # Paso 1: crear la empresa
    business_response = client.post("/businesses", json={
        "name": "Gómez Carpentry",
        "sector": "Manufacturing",
        "monthly_revenue": 5000
    })
    business_id = business_response.json()["id"]

    # Paso 2: mandar los datos de diagnóstico usando ese id
    diagnose_response = client.post(f"/businesses/{business_id}/diagnose", json={
        "sales": {
            "monthly_revenue": 500,
            "target_revenue": 250,
            "revenue_growth_rate": -0.1,
            "average_ticket_value": 200,
            "churn_rate": 0.3
        },
        "traffic": {
            "total_visitors": 50,
            "conversion_rate": 0.3,
            "customer_acquisition_cost": 150,
            "primary_acquisition_channel": "Social Media",
            "bounce_rate": 0.7
        },
        "management": {
            "fixed_operational_costs": 5000,
            "variable_costs": 2000,
            "all_earning": 6000,
            "inventory_turnover": -100,
            "automation_score": 0.3,
            "administrative_waste_estimate": 100
        },
        "reputation": {
            "net_promoter_score": -10,
            "percentage_negative_reviews": 0.5,
            "refund_request_rate": 0.5,
            "sentiment_index": 0.3,
            "main_complaint_theme": "Slow delivery"
        }
    })

    assert diagnose_response.status_code == 200
    assert isinstance(diagnose_response.json()["issues"], list)
    