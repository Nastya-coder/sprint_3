def test_account(website):
    page_main = website.login()
    page_main.button_account().click()
    website.wait_for_url("/account/profile")
    assert website.current_url() == "https://stellarburgers.nomoreparties.site/account/profile" \
        and website.page('account').button_logout().is_displayed()


def test_constructor_from_account(website):
    website.login()
    page_account = website.open_page("account")
    website.wait_for_url("/account/profile")
    page_account.button_constructor().click()
    website.wait_for_url("/")
    assert website.current_url() == "https://stellarburgers.nomoreparties.site/" \
        and website.page('main').button_order().is_displayed()
    

def test_constructor_from_logo(website):
    website.login()
    page_account = website.open_page("account")
    website.wait_for_url("/account/profile")
    page_account.image_logo().click()
    website.wait_for_url("/")
    assert website.current_url() == "https://stellarburgers.nomoreparties.site/" \
        and website.page('main').button_order().is_displayed()


def test_logout(website):
    website.login()
    page_account = website.open_page("account")
    website.wait_for_url("/account/profile")
    page_account.button_logout().click()
    website.wait_for_url("/login")
    website.open_page("account")
    website.wait_for_url("/login")
    assert website.current_url() == "https://stellarburgers.nomoreparties.site/login" \
        and website.page('login').label_login().is_displayed()
