class OrderMessageMistake:

    NO_INGREDIENTS_ERROR = {
    "success": False,
    "message": "Ingredient ids must be provided"
    }

    UNAUTHORIZED_ERROR = {
        "success": False,
        "message": "You should be authorised"
    }

class UserMessageMistake:

    DIBLICATE_USER = {
    "success": False,
    "message": "User already exists"
    }

    REQUIRED_FIELD = {
    "success": False,
    "message": "Email, password and name are required fields"
    }

    INCORRENT_FIELD = {
    "success": False,
    "message": "email or password are incorrect"
    }
    
INVALID_INGREDIENTS = {"ingredients": ["12345", "56789"]}
LOGIN_ERROR_FIELD = '12345'