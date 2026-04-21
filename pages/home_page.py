from pages.base_page import BasePage

class HomePage(BasePage):

    def search_book(self, keyword):
        self.fill("#small-searchterms", keyword)
        self.page.press("#small-searchterms", "Enter")