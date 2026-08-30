from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    email = "newstudent@mergington.edu"
    activity = "Chess Club"

    signup_response = client.post(f"/activities/{activity}/signup?email={email}")
    assert signup_response.status_code == 200

    delete_response = client.delete(f"/activities/{activity}/participants?email={email}")

    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == f"Removed {email} from {activity}"
    assert email not in client.get("/activities").json()[activity]["participants"]


def test_unregister_participant_missing_email_returns_404():
    response = client.delete("/activities/Chess Club/participants?email=missing@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found in activity"
