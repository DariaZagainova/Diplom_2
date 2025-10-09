from faker import Faker

fake = Faker()

def generate_user_payload():

    user_payload = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.first_name()
    }
    return user_payload
