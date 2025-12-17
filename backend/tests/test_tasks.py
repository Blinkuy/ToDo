# tests/test_task_api.py
import pytest

from tests.factories import TaskFactory


@pytest.mark.asyncio
async def test_add_task(client, session):
    # ARRANGE
    payload = {
        "user_id": 101,
        "name": "Buy milk",
        "description": "2 liters, please",
    }

    # ACT
    response = await client.post("/task/add", json=payload)

    # ASSERT
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == 101
    assert data["name"] == "Buy milk"
    assert data["description"] == "2 liters, please"
    assert "id" in data
    assert "created_at" in data


@pytest.mark.asyncio
async def test_get_tasks_by_user(client, session):
    # ARRANGE
    user_id = 42
    await TaskFactory.create_async(
        session=session, user_id=user_id, name="Task 1", description="Desc 1"
    )
    await TaskFactory.create_async(
        session=session, user_id=user_id, name="Task 2", description="Desc 2"
    )
    await TaskFactory.create_async(session=session, user_id=999, name="Other", description="Other")

    # ACT
    response = await client.get("/task/get_all", params={"user_id": user_id})

    # ASSERT
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 2
    for task in tasks:
        assert task["user_id"] == user_id
        assert "created_at" in task


@pytest.mark.asyncio
async def test_delete_task_success(client, session):
    # ARRANGE
    task = await TaskFactory.create_async(
        session=session, user_id=1, name="To delete", description="..."
    )
    await session.commit()

    # ACT
    response = await client.delete("/task/delete", params={"task_id": task.id})

    # ASSERT
    assert response.status_code == 200
    assert response.json() == {"detail": "Task deleted successfully"}


@pytest.mark.asyncio
async def test_delete_task_not_found(client):
    # ACT
    response = await client.delete("/task/delete", params={"task_id": 999999})

    # ASSERT
    assert response.status_code == 200
    assert response.json() == {"detail": "Task not found"}
