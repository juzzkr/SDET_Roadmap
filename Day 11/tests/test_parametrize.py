import pytest

@pytest.mark.parametrize(
    "username, password, expected",
     [
        ("standard_user", "secret_sauce", "inventory.html"),
        ("locked_out_user", "secret_sauce", "Epic sadface"),  
        ("standard_user", "wrong_pass", "Epic sadface"),   
    ]
)

def test_login_case(page, username, password, expected):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", username)
    page.fill("#password", password)
    page.click("#login-button")
    
    if "html" in expected:
        assert expected in page.url
    else:
        assert expected in page.inner_text("[data-test='error']")
    
