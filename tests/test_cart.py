from pages.cart_page import CartPage

def test_add_to_cart(page):
    cart = CartPage(page)

    cart.open_books()
    cart.add_to_cart()
    cart.go_to_cart()

    assert "Shopping cart" in page.content()


def test_remove_from_cart(page):
    cart = CartPage(page)

    # पहले add करो (important)
    cart.open_books()
    cart.add_to_cart()

    cart.go_to_cart()
    cart.remove_item()

    assert "empty" in page.content().lower()