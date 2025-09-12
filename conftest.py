import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def pw():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="function")        
def browser(pw):
    browser = pw.chromium.launch(headless=False, slow_mo=700)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()
    
@pytest.fixture(scope="function")
def login(page):  
    def _do_login(username = "standard_user", password = "secret_sauce"):      
        page.goto("https://www.saucedemo.com/")
        page.fill("input[name='user-name']", username)
        page.fill("input[name='password']", password)
        page.click("input[id='login-button']")
        page.wait_for_selector(".inventory_list")
    return _do_login
 
    
    
    
        