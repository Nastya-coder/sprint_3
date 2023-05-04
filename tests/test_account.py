from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions


# Helper functions

def login(driver):
    login_email = driver.find_element(By.NAME, "name")
    login_email.send_keys("nastyaageenko1666@yandex.ru")
    login_password = driver.find_element(By.NAME, "Пароль")
    login_password.send_keys("666666")
    button_enter = driver.find_element(By.XPATH, ".//button[text() = 'Войти']")
    button_enter.click()
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/")) 


def login_and_show_account(driver):
    login(driver)
    driver.get("https://stellarburgers.nomoreparties.site/account")
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))


# Tests

def test_account(login_page):
    login(login_page)
    assert login_page.current_url == "https://stellarburgers.nomoreparties.site/"
    button_account = login_page.find_element(By.XPATH, ".//p[text() = 'Личный Кабинет']")
    button_account.click()
    WebDriverWait(login_page, 3).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/account/profile")) 
    assert login_page.current_url == "https://stellarburgers.nomoreparties.site/account/profile"
    login_page.quit()
    

def test_constructor_from_account(login_page):
    login_and_show_account(login_page)
    button_constructor = login_page.find_element(By.XPATH, ".//p[text() = 'Конструктор']//parent::a")
    button_constructor.click()
    WebDriverWait(login_page, 3).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/")) 
    assert login_page.current_url == "https://stellarburgers.nomoreparties.site/"
    login_page.quit()


def test_constructor_from_logo(login_page):
    login_and_show_account(login_page) 
    logo = login_page.find_element(By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']/a")
    logo.click()
    WebDriverWait(login_page, 3).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/")) 
    assert login_page.current_url == "https://stellarburgers.nomoreparties.site/"
    login_page.quit()


def test_logout(login_page):
    login_and_show_account(login_page)
    button_logout = login_page.find_element(By.XPATH, ".//button[text()='Выход']")
    button_logout.click()
    WebDriverWait(login_page, 3).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/login")) 
    assert login_page.current_url == "https://stellarburgers.nomoreparties.site/login"

    # Double-check by clicking the account button
    button_account = login_page.find_element(By.XPATH, ".//p[text() = 'Личный Кабинет']")
    button_account.click()
    WebDriverWait(login_page, 3).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/login")) 
    assert login_page.current_url == "https://stellarburgers.nomoreparties.site/login"
    login_page.quit()
