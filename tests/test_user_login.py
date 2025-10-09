import pytest
import allure
from methods.user_methods import UserMethod
from data import UserMessageMistake

@allure.sub_suite('class TestUserLogin: Логин пользователя')
class TestUserLogin:


    @allure.title('Вход под существующим пользователем')
    @allure.description('Можно залогиниться, введя валидные email и пароль')
    def test_success_login_user(self, create_user):
        login_user_response = UserMethod.login_user(create_user['user_data_for_login'])
        with allure.step("Проверяем статус кода ответа"):
            assert login_user_response.status_code == 200
        with allure.step("Проверяем тело ответа"):
            assert login_user_response.json()["success"] == True
            assert "accessToken" in login_user_response.json() and login_user_response.json()["accessToken"].startswith("Bearer ")
            assert "refreshToken" in login_user_response.json() and len(login_user_response.json()["refreshToken"]) > 0
            assert "user" in login_user_response.json() and login_user_response.json()["user"]["email"] == create_user['user_data_for_login']["email"] and login_user_response.json()["user"]["name"] == create_user['user_data']["name"]

  
    @allure.title('Вход с неверным логином или паролем')
    @allure.description('Нельзя залогиниться, если ввести неверный email или пароль')
    @pytest.mark.parametrize('error_field', ['email', 'password'])
    def test_user_cannot_login_with_error_login_or_password(self, create_user, error_field):
        user_data_for_login = create_user['user_data_for_login'].copy()
        user_data_for_login[error_field] = '12345'
        login_user_response = UserMethod.login_user(user_data_for_login)
        with allure.step("Проверяем статус кода ответа"):
            assert login_user_response.status_code == 401
        with allure.step("Проверяем сообщение об ошибке"):    
            assert login_user_response.json() == UserMessageMistake.INCORRENT_FIELD
    