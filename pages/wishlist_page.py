from pages.base_page import BasePage

class WishlistPage(BasePage):

    def open_books(self):
        self.page.goto("http://demowebshop.tricentis.com/books")

    def add_to_wishlist(self):
        # product open करो
        self.page.locator(".product-title a").first.click()

        # product page पर wishlist
        self.page.locator("#add-to-wishlist-button-13").click()

    def open_wishlist(self):
        self.page.goto("http://demowebshop.tricentis.com/wishlist")