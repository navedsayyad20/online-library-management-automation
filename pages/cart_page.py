from pages.base_page import BasePage

class CartPage(BasePage):

    def open_books(self):
        self.page.goto("http://demowebshop.tricentis.com/books")

    def add_to_cart(self):
        # multiple buttons → first use
        self.page.locator("input[value='Add to cart']").first.click()

    def go_to_cart(self):
        self.page.goto("http://demowebshop.tricentis.com/cart")

    def remove_item(self):
        # wait + safe remove
        if self.page.locator("input[name='removefromcart']").count() > 0:
            self.page.locator("input[name='removefromcart']").first.check()
            self.page.locator("input[name='updatecart']").click()