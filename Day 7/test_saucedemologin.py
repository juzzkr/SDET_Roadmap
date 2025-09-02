from playwright.sync_api import sync_playwright

def test_saucedemologin():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")

        page.fill("input[name='user-name']", "standard_user")
        page.fill("input[name='password']", "secret_sauce")
        page.keyboard.press("Enter")

        assert page.url == "https://www.saucedemo.com/inventory.html"

        browser.close()
