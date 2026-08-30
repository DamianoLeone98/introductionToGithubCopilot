def test_unregister_participant_for_missing_activity_returns_404(client):
    # Arrange
    activity = "Nonexistent Club"
    email = "michael@mergington.edu"

    # Act
    from urllib.parse import quote

    response = client.delete(f"/activities/{quote(activity)}/participants?email={quote(email)}")
    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
