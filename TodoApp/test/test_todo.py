import pytest

pytestmark = pytest.mark.anyio


async def test_read_all_authenticated(client, test_data):
    response = await client.get("/todo/")
    response_data = response.json()
    assert response.status_code == 200
    # Admin only has two todos
    assert len(response_data) == 2
