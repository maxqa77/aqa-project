import requests
from utils.logger import get_logger

logger = get_logger(__name__)

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_posts(self):
        url = f"{self.base_url}/posts"
        logger.info(f"GET {url}")

        response = requests.get(url)

        logger.info(f"Status: {response.status_code}")
        return response
