import pytest
from generators import generate_user_payload
from methods.user_methods import UserMethod


# Генерация данных пользователя; после теста удаление пользователя
@pytest.fixture
def user_payload():
    user_data = generate_user_payload()   
    yield user_data
    user_data_for_login = {
        "email": user_data["email"],             
        "password": user_data["password"]
    }
    login_user = UserMethod.login_user(user_data_for_login)
    access_token = UserMethod.access_token_login_user(login_user)
    UserMethod.delete_user(access_token)


# Создание пользователя; возвращает данные, данные для логина и токен; удаление после теста
@pytest.fixture
def create_user():
    user_data = generate_user_payload() 
    user_data_create = UserMethod.create_user(user_data)
    user_data_for_login = {
        "email": user_data["email"],
        "password": user_data["password"]
    }
    access_token = UserMethod.access_token_create_user(user_data_create)
    yield {
        'user_data': user_data ,
        'user_data_for_login': user_data_for_login,
        'access_token': access_token
    }
    UserMethod.delete_user(access_token)


# Авторизация пользователя, возвращает accessToken
@pytest.fixture
def login_user(create_user):
    user_data_for_login = create_user['user_data_for_login']
    login_user = UserMethod.login_user(user_data_for_login)
    access_token = UserMethod.access_token_login_user(login_user)
    return access_token
