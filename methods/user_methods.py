import requests
import urls
import allure


class UserMethod:

    @staticmethod
    @allure.step('Создаём пользователя')
    def create_user(user_payload):
        create_user_response = requests.post(urls.URL_CREATE_USER, json=user_payload)
        return create_user_response
    
    @staticmethod
    @allure.step('Получаем accessToken у созданного пользователя')
    def access_token_create_user(create_user_response):
        access_token_user = create_user_response.json().get('accessToken') 
        return access_token_user   

    @staticmethod
    @allure.step('Авторизация пользователя')
    def login_user(user_data):
        login_user_response = requests.post(urls.URL_LOGIN_USER, json=user_data)
        return login_user_response

    @staticmethod
    @allure.step('Получаем accessToken у авторизованного пользователя')
    def access_token_login_user(login_user_response):
        access_token_user = login_user_response.json().get('accessToken') 
        return access_token_user   

    @staticmethod
    @allure.step('Удаляем пользователя')
    def delete_user(access_token_user):
        headers = {"Authorization": access_token_user}
        delete_user_response = requests.delete(urls.URL_DELETE_USER, headers=headers)
        return delete_user_response