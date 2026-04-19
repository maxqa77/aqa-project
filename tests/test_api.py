import pytest
import allure
from api.client import APIClient


@allure.feature("ВАЛЕРА")
@allure.story("Хватит Дрыхнуть")
@allure.title("ВАЛЕРА или ЛЕРА?")
@allure.description("ВАЛЕРА или ЛЕРА?")

@pytest.mark.api
def test_get_posts(base_url):

    with allure.step("ВАЛЕРА"):
        client = APIClient(base_url)

    with allure.step("ВАЛЕРА или ЛЕРА?"):
        response = client.get_posts()

    with allure.step("Проверяем статус код 200"):
        assert response.status_code == 200
