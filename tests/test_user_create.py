import pytest
import allure
from methods.user_methods import UserMethod
from data import UserMessageMistake


@allure.sub_suite('class TestUserCreate: Создание пользователя')
class TestUserCreate:

    @allure.title('Уникального пользователя можно создать')
    def test_success_create_user(self, user_payload):
        create_user_response = UserMethod.create_user(user_payload)
        with allure.step("Проверяем статус кода ответа"):
            assert create_user_response.status_code == 200
        with allure.step("Проверяем тело ответа"):  
            assert create_user_response.json()["success"] == True
            assert "user" in create_user_response.json() and create_user_response.json()["user"]["email"] == user_payload["email"] and create_user_response.json()["user"]["name"] == user_payload["name"]
            assert "accessToken" in create_user_response.json() and create_user_response.json()["accessToken"].startswith("Bearer ")
            assert "refreshToken" in create_user_response.json() and len(create_user_response.json()["refreshToken"]) > 0

    
    @allure.title('Нельзя создать пользователя, который уже зарегистрирован')
    def test_duplicate_user_creation_fail(self, user_payload):
        UserMethod.create_user(user_payload)
        create_dublicate_user_response = UserMethod.create_user(user_payload)
        with allure.step("Проверяем статус кода ответа"):
            assert create_dublicate_user_response.status_code == 403
        with allure.step("Проверяем сообщение об ошибке"):   
            assert create_dublicate_user_response.json() == UserMessageMistake.DIBLICATE_USER


    @allure.title("Нельзя создать пользователя без имени, email или пароля")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_cannot_create_courier_without_login_or_password_or_name(self, user_payload, missing_field):
        user_data = user_payload.copy()
        user_data.pop(missing_field)
        create_user_response = UserMethod.create_user(user_data)
        with allure.step("Проверяем статус кода ответа"):
            assert create_user_response.status_code == 403
        with allure.step("Проверяем сообщение об ошибке"):  
            assert create_user_response.json() == UserMessageMistake.REQUIRED_FIELD
