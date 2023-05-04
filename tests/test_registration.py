from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions


def test_registration(registration_page):
    login_details = registration_page.find_elements(By.NAME, "name")
    login_details[0].send_keys("Nastya")   # Login
    login_details[1].send_keys("nastyaageenko16667@yandex.ru")   # Email
    password = registration_page.find_element(By.XPATH, ".//input[@type='password']")
    password.send_keys("666666")
    register = registration_page.find_element(By.XPATH, ".//button[text() = 'Зарегистрироваться']")
    register.click()
    WebDriverWait(registration_page, 3).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/login")) 
    assert registration_page.current_url == 'https://stellarburgers.nomoreparties.site/login'
    registration_page.quit()


def test_incorrect_password(registration_page):
    password = registration_page.find_element(By.XPATH, ".//input[@type='password']")
    password.send_keys("333")
    register = registration_page.find_element(By.XPATH, ".//button[text() = 'Зарегистрироваться']")
    register.click()
    error = registration_page.find_element(By.XPATH, ".//p[@class='input__error text_type_main-default']")
    assert error
    registration_page.quit()
