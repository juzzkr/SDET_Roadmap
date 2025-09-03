from playwright.sync_api import sync_playwright

def test_prdocts_sauce():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        page.fill("input[name='user-name']", "standard_user")
        page.fill("input[name='password']", "secret_sauce")
        page.keyboard.press("Enter")
        
        assert page.url == "https://www.saucedemo.com/inventory.html"
        assert page.inner_text(".title") == "Products"
        
        items = page.query_selector_all(".inventory_item_name")
        print(f"It has {len(items)} products")
        for item in items:
            print("Product:", item.inner_text()) 
        page.screenshot(path= "Day 8/products_page.png")
        browser.close()
            
            
 