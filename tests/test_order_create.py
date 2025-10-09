import pytest
import allure
from methods.order_methods import OrderMethod
from data import OrderMessageMistake


@allure.sub_suite('class TestOrderCreate: Создание заказа')
class TestOrderCreate:


    @allure.title('Создание заказа с авторизацией и с игредиентами')
    def test_create_order_login_user_with_ingredients(self, login_user):
        access_token = login_user
        ingredients_id = OrderMethod.get_ingredients_id()
        selected_ingredients = ingredients_id[:3]
        create_order_response = OrderMethod.create_order(access_token, selected_ingredients)
        with allure.step("Проверяем статус кода ответа"):
            assert create_order_response.status_code == 200
        with allure.step("Проверяем тело ответа"):
            assert "name" in create_order_response.json() and len(create_order_response.json()["name"]) > 0
            assert "order" in create_order_response.json() and "number" in create_order_response.json()["order"] and create_order_response.json()["order"]["number"] > 0
            assert create_order_response.json()["success"] == True

    @allure.title('Создание заказа без авторизации и с игредиентами')
    @allure.description('Можно создать заказ, если пользователь авторизован и в зазаз добавлены ингредиенты')
    def test_create_order_user_without_login_with_ingredients(self):
        ingredients_id = OrderMethod.get_ingredients_id()
        selected_ingredients = ingredients_id[:3]
        create_order_response = OrderMethod.create_order(None, selected_ingredients)
        with allure.step("Проверяем статус кода ответа"):
            assert create_order_response.status_code == 403

    @allure.title('Cоздание заказа с авторизацией и без игредиентов')
    @allure.description('Нельзя создать заказ, если пользователь авторизован, но в заказ не добавлены ингредиенты')
    def test_not_create_order_login_user_without_ingredients(self, login_user):
        access_token = login_user
        create_order_response = OrderMethod.create_order(access_token, [])
        with allure.step("Проверяем статус кода ответа"):
            assert create_order_response.status_code == 400
        with allure.step("Проверяем сообщение об ошибке"): 
            assert create_order_response.json() ==  OrderMessageMistake.NO_INGREDIENTS_ERROR

    @allure.title('Cоздание заказа без авторизации и без игредиентов')
    @allure.description('Нельзя создать заказ, если пользователь не авторизован и в зазаз не добавлены ингредиенты')
    def test_not_create_order_without_login_without_ingredients(self):
        access_token = None
        create_order_response = OrderMethod.create_order(access_token, [])
        with allure.step("Проверяем статус кода ответа"):
            assert create_order_response.status_code == 400
        with allure.step("Проверяем сообщение об ошибке"):
            assert create_order_response.json() ==  OrderMessageMistake.NO_INGREDIENTS_ERROR

    @allure.title('Cоздание заказа с неверным хешем ингредиентов, с авторизацией')
    @allure.description('Нельзя создать заказ, если пользователь авторизован, но в заказе неверный хеш ингредиентов')
    def test_not_create_order_login_user_with_error_ingredients(self, login_user):
        access_token = login_user
        selected_ingredients = {"ingredients": ["12345", "56789"]}
        create_order_response = OrderMethod.create_order(access_token, selected_ingredients)
        with allure.step("Проверяем статус кода ответа"):
            assert create_order_response.status_code == 500
