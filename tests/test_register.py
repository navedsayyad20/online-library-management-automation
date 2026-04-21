from pages.register_page import RegisterPage
from utils.random_data import generate_email

def test_register(page):
    register = RegisterPage(page)

    email = generate_email()
    password = "Test@123"

    register.open_register()
    register.register_user(email, password)

    assert register.is_registration_successful()