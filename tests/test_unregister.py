def test_unregister_participant_for_missing_activity_returns_404(client):
    # Arrange
    activity = "Nonexistent Club"
    email = "michael@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity}/participants?email={email}")

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
