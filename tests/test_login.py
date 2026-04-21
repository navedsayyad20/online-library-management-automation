import pytest
from pages.login_page import LoginPage

@pytest.mark.skip(reason="Skipping due to unstable login on demo site")
def test_login(page):
    login = LoginPage(page)

    login.open_login()
    login.login("test123@gmail.com", "Test@123")

    assert "Log out" in page.content()