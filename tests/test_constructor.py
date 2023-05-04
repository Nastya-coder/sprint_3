from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


# Helper functions

def button_selected(element):
    return element.get_attribute("class") == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"


# Tests

def test_bun(main_page):
    button_bun = main_page.find_element(By.XPATH, ".//span[text()='Булки']//parent::div")
    assert button_selected(button_bun)
    
    # Bun button is selected by default so in order to test it
    # we need to select some other section first
    button_sauce = main_page.find_element(By.XPATH, ".//span[text()='Соусы']//parent::div")
    button_sauce.click() 

    # Now we can click the bun button
    assert not button_selected(button_bun)
    button_bun.click()

    # Check the visibility of the section
    label_bun = main_page.find_element(By.XPATH, ".//h2[text()='Булки']")
    WebDriverWait(main_page, 3).until(expected_conditions.visibility_of(label_bun))
    assert label_bun.is_displayed()
    
    # And the clickability of the buttons
    assert button_selected(button_bun)
    assert not button_selected(button_sauce)
    main_page.quit()


def test_sauce(main_page):
    button_sauce = main_page.find_element(By.XPATH, ".//span[text()='Соусы']//parent::div")
    assert not button_selected(button_sauce)
    button_sauce.click() 
    label_sauce = main_page.find_element(By.XPATH, ".//h2[text()='Соусы']")
    WebDriverWait(main_page, 3).until(expected_conditions.visibility_of(label_sauce))
    assert button_selected(button_sauce)
    assert label_sauce.is_displayed()
    main_page.quit()


def test_filling(main_page):
    button_filling = main_page.find_element(By.XPATH, ".//span[text()='Начинки']//parent::div")
    assert not button_selected(button_filling)
    button_filling.click()
    label_filling = main_page.find_element(By.XPATH, ".//h2[text()='Начинки']")
    WebDriverWait(main_page, 3).until(expected_conditions.visibility_of(label_filling))
    assert button_selected(button_filling)
    assert label_filling.is_displayed()
    main_page.quit()
