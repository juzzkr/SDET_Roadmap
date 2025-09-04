def test_addcart(page, login):
    login()
    page.click("button[name='add-to-cart-sauce-labs-backpack']")
    page.inner_text(".shopping_cart_badge") == 1