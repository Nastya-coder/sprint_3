from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions

from config import *


class StellarBurgersPageMain:

    def __init__(self, driver):
        self.url = ""
        self.driver = driver

    def button_selected(self, element):
        return element.get_attribute("class") == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"         

    # Locators
    # Войти в аккаунт
    def button_login(self):
        return self.driver.find_element(By.XPATH, ".//button[text() = 'Войти в аккаунт']")
    
    # Личный кабинет
    def button_account(self):
        return self.driver.find_element(By.XPATH, ".//p[text() = 'Личный Кабинет']")
    
    # Оформить заказ
    def button_order(self):
        return self.driver.find_element(By.XPATH, ".//button[text() = 'Оформить заказ']")
    
    # Кнопка булки
    def button_bun(self):
        return self.driver.find_element(By.XPATH, ".//span[text()='Булки']//parent::div")
    
    # Кнопка соусы
    def button_sauce(self):
        return self.driver.find_element(By.XPATH, ".//span[text()='Соусы']//parent::div")
    
    # Кнопка начинки
    def button_filling(self):
        return self.driver.find_element(By.XPATH, ".//span[text()='Начинки']//parent::div")

    # Секция булки
    def label_bun(self):
        return self.driver.find_element(By.XPATH, ".//h2[text()='Соусы']")

    # Секция соусы
    def label_sauce(self):
        return self.driver.find_element(By.XPATH, ".//h2[text()='Начинки']")

    # Секция начинки
    def label_filling(self):
        return self.driver.find_element(By.XPATH, ".//h2[text()='Начинки']")


class StellarBurgersPageRegistration:

    def __init__(self, driver):
        self.url = "/register"
        self.driver = driver

    # Locators
    # Имя
    def input_name(self):
        login_details = self.driver.find_elements(By.NAME, "name")
        return login_details[0]

    # Email
    def input_email(self):
        login_details = self.driver.find_elements(By.NAME, "name")
        return login_details[1]

    # Пароль
    def input_password(self):
        return self.driver.find_element(By.XPATH, ".//input[@type = 'password']")

    # Зарегистрироваться
    def button_register(self):
        return self.driver.find_element(By.XPATH, ".//button[text() = 'Зарегистрироваться']")
    
    # Войти
    def button_login(self):
        return self.driver.find_element(By.XPATH, ".//a[text() = 'Войти']")
    
    # Некорректынй пароль
    def label_error(self):
        return self.driver.find_element(By.XPATH, ".//p[@class = 'input__error text_type_main-default']")    

    
class StellarBurgersPageLogin:

    def __init__(self, driver):
        self.url = "/login"
        self.driver = driver

    # Locators
    # Логин
    def input_email(self):
        return self.driver.find_element(By.NAME, "name")
    
    # Пароль
    def input_password(self):
        return self.driver.find_element(By.NAME, "Пароль")
    
    # Войти
    def button_login(self):
        return self.driver.find_element(By.XPATH, ".//button[text() = 'Войти']")
    
    # Вход
    def label_login(self):
        return self.driver.find_element(By.XPATH, ".//h2[text() = 'Вход']")

    
class StellarBurgersPageForgotPassword:

    def __init__(self, driver):
        self.url = "/forgot-password"
        self.driver = driver
        
    # Locators
    # Bойти
    def button_login(self):
        return self.driver.find_element(By.XPATH, ".//a[text() = 'Войти']")


class StellarBurgersPageAccount:

    def __init__(self, driver):
        self.url = "/account"
        self.driver = driver

    # Locators
    # Конструктор
    def button_constructor(self):
        return self.driver.find_element(By.XPATH, ".//p[text() = 'Конструктор']//parent::a")
    
    # Выход
    def button_logout(self):
        return self.driver.find_element(By.XPATH, ".//button[text() = 'Выход']")    
    
    # Логотип
    def image_logo(self):
        return self.driver.find_element(By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']/a")


class StellarBurgers:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = "https://stellarburgers.nomoreparties.site"
        self._pages = {
            "main" : StellarBurgersPageMain(self.driver),
            "registration" : StellarBurgersPageRegistration(self.driver),
            "login" : StellarBurgersPageLogin(self.driver),
            "forgot" : StellarBurgersPageForgotPassword(self.driver),
            "account" : StellarBurgersPageAccount(self.driver),
        }

    def wait_for_url(self, sub_url):
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(self.url + sub_url))        

    def wait_until_visible(self, element):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of(element))

    def page(self, name):
        return self._pages[name]

    def open_page(self, name):
        page = self.page(name)
        self.driver.get(self.url + page.url)
        return page
    
    def current_url(self):
        return self.driver.current_url
    
    def login(self):
        page_login = self.open_page("login")
        page_login.input_email().send_keys(REGISTRATION_EMAIL)
        page_login.input_password().send_keys(REGISTRATION_PASSWORD)
        page_login.button_login().click()
        self.wait_for_url("/")
        return self.page("main")
    
    def quit(self):
        return self.driver.quit()
