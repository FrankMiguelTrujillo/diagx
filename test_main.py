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