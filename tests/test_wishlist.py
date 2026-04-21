import pytest
from pages.wishlist_page import WishlistPage

@pytest.mark.skip(reason="Wishlist feature unstable on demo site")
def test_wishlist(page):
    wish = WishlistPage(page)

    wish.open_home()
    wish.add_to_wishlist()
    wish.open_wishlist()

    assert "Wishlist" in page.content()