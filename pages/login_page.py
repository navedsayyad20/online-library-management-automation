from pages.base_page import BasePage

class LoginPage(BasePage):

    def open_login(self):
        self.page.goto("http://demowebshop.tricentis.com/login")

    def login(self, email, password):
        self.fill("#Email", email)
        self.fill("#Password", password)
        # correct button locator
        self.page.locator("input[value='Log in']").click()