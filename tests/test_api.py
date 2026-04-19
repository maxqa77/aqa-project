import pytest
import allure
from api.client import APIClient


@allure.feature("ВАЛЕРА")
@allure.story("Хватит Дрыхнуть")
@allure.title("📄 Проверка получения списка постов (200 OK)")
@allure.description("API должен вернуть список постов со статусом 200")

@pytest.mark.api
def test_get_posts(base_url):

    with allure.step("ВАЛЕРА"):
        client = APIClient(base_url)

    with allure.step("Отправляем запрос GET /posts"):
        response = client.get_posts()

    with allure.step("Проверяем статус код 200"):
        assert response.status_code == 200
