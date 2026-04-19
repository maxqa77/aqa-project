from api.client import APIClient

def test_get_posts(base_url):
    client = APIClient(base_url)
    response = client.get_posts()

    assert response.status_code == 200
