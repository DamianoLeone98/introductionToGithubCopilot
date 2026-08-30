def test_get_activities_returns_expected_structure(client):
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    body = response.json()
    assert expected_activity in body
    activity = body[expected_activity]
    assert set(activity.keys()) == {"description", "schedule", "max_participants", "participants"}
    assert isinstance(activity["participants"], list)
