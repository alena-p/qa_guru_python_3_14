from selene import have

from model import cart
from selene.support.shared import browser


def test_verify_counter_after_adding():
    customer = cart.add_product_to_cart_via_list("31/1/1")
    browser.open("/Themes/DefaultClean/Content/images/logo.png")
    browser.driver.add_cookie({"name": "Nop.customer", "value": customer})
    browser.open("")
    browser.element(".cart-qty").should(have.text("1"))


def test_verify_cart_clearing():
    customer = cart.add_product_to_cart_via_list("31/1/1")
    browser.open("/Themes/DefaultClean/Content/images/logo.png")
    browser.driver.add_cookie({"name": "Nop.customer", "value": customer})
    browser.open("/cart")
    browser.element(".remove-from-cart input").click()
    browser.element(".update-cart-button").click()
    browser.element(".order-summary-content").should(
        have.text("Your Shopping Cart is empty!")
    )


def test_verify_cart_deleting_item():
    customer = cart.add_product_to_cart_via_list("31/1/1")
    cart.add_product_to_cart_via_list("/36/1/1", customer)
    browser.open("/Themes/DefaultClean/Content/images/logo.png")
    browser.driver.add_cookie({"name": "Nop.customer", "value": customer})
    browser.open("/cart")
    assert len(browser.elements(".cart-item-row")) == 2
    browser.elements(".remove-from-cart").first.click()
    browser.element(".update-cart-button").click()
    assert len(browser.elements(".cart-item-row")) == 1


def test_verify_changing_qty():
    customer = cart.add_product_to_cart_via_list("14/1/1")
    browser.open("/Themes/DefaultClean/Content/images/logo.png")
    browser.driver.add_cookie({"name": "Nop.customer", "value": customer})
    browser.open("/cart")
    browser.element(".qty-input").click().set("2")
    browser.element(".update-cart-button").click()
    browser.open("/cart")
    browser.element(".qty-input").should(have.value("2"))
