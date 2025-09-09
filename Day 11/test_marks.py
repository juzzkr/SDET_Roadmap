import pytest

def test_login_valid(page, login):
    login()
    assert page.url.endswith("/inventory.html")
    
@pytest.mark.smoke
def test_add_to_cart(page, login):
    login()
    page.click("#add-to-cart-sauce-labs-backpack")
    assert page.inner_text(".shopping_cart_badge")
    
@pytest.mark.regression
def test_logout(page, login):
    login()
    page.click("#react-burger-menu-btn")
    page.click("#logout_sidebar_link")
    assert page.url == "https://www.saucedemo.com/"