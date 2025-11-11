BASE_URL = "https://stellarburgers.education-services.ru"

# Пользователь
URL_CREATE_USER = f"{BASE_URL}/api/auth/register" # Создание пользователя
URL_LOGIN_USER = f"{BASE_URL}/api/auth/login" # Авторизация пользователя
URL_DELETE_USER = f"{BASE_URL}/api/auth/user" # Удаление пользователя

# Заказ
URL_GET_INGREDIENTS = f"{BASE_URL}/api/ingredients" # Получение данных об иингредиентах
URL_CREATE_ORDER = f"{BASE_URL}/api/orders" # Создание заказ
