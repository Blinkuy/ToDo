import pytest

from tests.factories import TaskFactory, UserFactory


@pytest.mark.asyncio
async def test_get_tasks_success(client, session):
    # Arrange
    user = UserFactory()
    session.add(user)
    await session.commit()

    task = TaskFactory.build(
        user_id=user.id,
        name="Test task",
        description="Test description",
    )
    session.add(task)
    await session.commit()

    # Act
    response = await client.get(f"/task/get_all?user_id={user.id}")

    # Assert
    assert response.status_code == 200

    expected = [
        {
            "id": task.id,
            "name": "Test task",
            "description": "Test description",
            "created_at": response.json()[0]["created_at"],
        }
    ]

    assert response.json() == expected
