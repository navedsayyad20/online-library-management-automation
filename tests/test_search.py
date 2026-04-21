from pages.home_page import HomePage

def test_search(page):
    home = HomePage(page)

    page.goto("http://demowebshop.tricentis.com")
    home.search_book("book")

    assert "Books" in page.content()