from pages.base_page import BasePage

class RegisterPage(BasePage):

    def open_register(self):
        self.page.goto("http://demowebshop.tricentis.com/register")

    def register_user(self, email, password):
        self.page.locator("#gender-male").click()
        self.page.fill("#FirstName", "Test")
        self.page.fill("#LastName", "User")
        self.page.fill("#Email", email)
        self.page.fill("#Password", password)
        self.page.fill("#ConfirmPassword", password)
        self.page.locator("#register-button").click()

    def is_registration_successful(self):
        # success message visible
        return self.page.locator(".result").is_visible()