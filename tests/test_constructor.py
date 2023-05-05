def test_bun(website):
    # Bun button is selected by default so in order to test it we need to select some other section first
    page_main = website.open_page("main")
    page_main.button_sauce().click()
    
    # Now we can click the bun button
    page_main.button_bun().click()
    website.wait_until_visible(page_main.label_bun())
    assert page_main.label_bun().is_displayed() and page_main.button_selected(page_main.button_bun())


def test_sauce(website):
    page_main = website.open_page("main")
    page_main.button_sauce().click()
    website.wait_until_visible(page_main.label_sauce())
    assert page_main.label_sauce().is_displayed() and page_main.button_selected(page_main.button_sauce())


def test_filling(website):
    page_main = website.open_page("main")
    page_main.button_filling().click()
    website.wait_until_visible(page_main.label_filling())
    assert page_main.label_filling().is_displayed() and page_main.button_selected(page_main.button_filling())
