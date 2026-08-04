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
    assert response["name"] == str
    # tu turno: agregá un assert más, verificando algo del contenido de la respuesta