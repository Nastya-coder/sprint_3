def test_login(website):
    website.login()
    assert website.current_url() == "https://stellarburgers.nomoreparties.site/" \
        and website.page('main').button_order().is_displayed()
    

def test_login_main_page(website):
    page_main = website.open_page("main")
    page_main.button_login().click()
    website.wait_for_url("/login")
    assert website.current_url() == "https://stellarburgers.nomoreparties.site/login" \
        and website.page('login').label_login().is_displayed()
    test_login(website)


def test_login_account_button(website):
    page_main = website.open_page("main")
    page_main.button_account().click()
    website.wait_for_url("/login")
    assert website.current_url() == "https://stellarburgers.nomoreparties.site/login" \
        and website.page('login').label_login().is_displayed()
    test_login(website)    


def test_login_registration(website):
    page_registration = website.open_page("registration")
    page_registration.button_login().click()
    website.wait_for_url("/login")
    assert website.current_url() == "https://stellarburgers.nomoreparties.site/login" \
        and website.page('login').label_login().is_displayed()
    test_login(website)      


def test_login_forgot_password_page(website):
    page_forgot = website.open_page("forgot")
    page_forgot.button_login().click()
    website.wait_for_url("/login")
    assert website.current_url() == "https://stellarburgers.nomoreparties.site/login" \
        and website.page('login').label_login().is_displayed()
    test_login(website)  
