class OrderMessageMistake:

    NO_INGREDIENTS_ERROR = {
    "success": False,
    "message": "Ingredient ids must be provided"
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
    