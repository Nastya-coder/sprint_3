import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def main_page():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")
    return driver


@pytest.fixture
def registration_page():
    driver = webdriver.Chrome()    
    driver.get("https://stellarburgers.nomoreparties.site/register")
    return driver


@pytest.fixture
def login_page():
    driver = webdriver.Chrome()    
    driver.get("https://stellarburgers.nomoreparties.site/login")
    return driver


@pytest.fixture
def forgot_password_page():
    driver = webdriver.Chrome()    
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    return driver


@pytest.fixture
def forgot_account_page():
    driver = webdriver.Chrome()    
    driver.get("https://stellarburgers.nomoreparties.site/account")
    return driver
