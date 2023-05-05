from config import *

def test_registration(website):
    registration = website.open_page("registration")
    registration.input_name().send_keys(REGISTRATION_NAME)
    registration.input_email().send_keys(REGISTRATION_EMAIL)
    registration.input_password().send_keys(REGISTRATION_PASSWORD)
    registration.button_register().click()
    website.wait_for_url("/login")
    assert website.current_url() == "https://stellarburgers.nomoreparties.site/login" \
        and website.page('login').label_login().is_displayed()


def test_incorrect_password(website):
    registration = website.open_page("registration")
    registration.input_password().send_keys("333")
    registration.button_register().click()
    assert registration.label_error()
