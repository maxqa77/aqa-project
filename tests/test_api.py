import pytest
from api.client import APIClient

@pytest.mark.api
def test_get_posts(base_url):
    client = APIClient(base_url)
    response = client.get_posts()
    assert response.status_code == 200
