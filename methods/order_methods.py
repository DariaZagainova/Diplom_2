import requests
import urls
import allure


class OrderMethod:

    @staticmethod
    @allure.step('Получаем id ингредиентoв')
    def get_ingredients_id():
        ingredients_list = requests.get(urls.URL_GET_INGREDIENTS).json().get('data')
        ingredients_id = []

        for item in ingredients_list:
            ingredients_id.append(item.get('_id'))        

        return ingredients_id


    @staticmethod
    @allure.step('Создаём заказ')
    def create_order(access_token_user, ingredients_id):
        headers = {"Authorization": access_token_user}
        ingredients_payload = {
            "ingredients": ingredients_id
        }
        create_order_response = requests.post(urls.URL_CREATE_ORDER, headers=headers, json=ingredients_payload)
        return create_order_response
    