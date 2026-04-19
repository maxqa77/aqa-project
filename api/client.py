import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_posts(self):
        return requests.get(f"{self.base_url}/posts")
