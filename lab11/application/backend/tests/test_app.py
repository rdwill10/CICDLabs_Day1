from app.app import app

def test_home():
    client = app.test_client()
    rv = client.get("/")
    assert rv.status_code == 200
    assert b"Hello" in rv.data

def test_health():
    client = app.test_client()
    rv = client.get("/api/health")
    assert rv.status_code == 200
    data = rv.get_json()
    assert data["status"] == "healthy"
