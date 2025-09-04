def test_login(page, login):
    login()
    assert page.url == "https://www.saucedemo.com/inventory.html"
    assert page.inner_text(".title") == "Products"