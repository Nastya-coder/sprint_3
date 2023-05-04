from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions


def test_login(login_page):
    login_email = login_page.find_element(By.NAME, "name")
    login_email.send_keys("nastyaageenko1666@yandex.ru")
    login_password = login_page.find_element(By.NAME, "Пароль")
    login_password.send_keys("666666")
    button_enter = login_page.find_element(By.XPATH, ".//button[text() = 'Войти']")
    button_enter.click()
    WebDriverWait(login_page, 3).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/")) 
    assert login_page.current_url == "https://stellarburgers.nomoreparties.site/"
    login_page.quit()
    

def test_login_main_page(main_page):
    login = main_page.find_element(By.XPATH, ".//button[text() = 'Войти в аккаунт']")
    login.click()
    WebDriverWait(main_page, 3).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/login")) 
    assert main_page.current_url == "https://stellarburgers.nomoreparties.site/login"
    test_login(main_page)


def test_login_account_button(main_page):
    button_account = main_page.find_element(By.XPATH, ".//p[text() = 'Личный Кабинет']")
    button_account.click()
    WebDriverWait(main_page, 3).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/login")) 
    assert main_page.current_url == "https://stellarburgers.nomoreparties.site/login"
    test_login(main_page)


def test_login_registration(registration_page):
    button_account = registration_page.find_element(By.XPATH, ".//a[text() = 'Войти']")
    button_account.click()
    WebDriverWait(registration_page, 3).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/login")) 
    assert registration_page.current_url == "https://stellarburgers.nomoreparties.site/login"
    test_login(registration_page)


def test_login_forgot_password_page(forgot_password_page):
    button_account = forgot_password_page.find_element(By.XPATH, ".//a[text() = 'Войти']")
    button_account.click()
    WebDriverWait(forgot_password_page, 3).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/login")) 
    assert forgot_password_page.current_url == "https://stellarburgers.nomoreparties.site/login"
    test_login(forgot_password_page)
