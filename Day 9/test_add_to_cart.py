from playwright.sync_api import sync_playwright

def test_prdocts_sauce():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        page.fill("input[name='user-name']", "standard_user")
        page.fill("input[name='password']", "secret_sauce")
        page.keyboard.press("Enter")
        
        page.click("button[name='add-to-cart-sauce-labs-backpack']")
        
        assert page.inner_text(".shopping_cart_badge") == "1"
        
        page.locator(".shopping_cart_link").screenshot(path="Day 9/cart_icon.png")
        
        browser.close()