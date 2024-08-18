from app.core import settings
from fastapi.testclient import TestClient


def test_health_check_ok(client: TestClient):
    response = client.get(f"{settings.API_STR}/")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
