import allure
from selene import have

from model import cart
from selene.support.shared import browser


def test_verify_counter_after_adding():
    with allure.step("Add product to cart"):
        customer = cart.add_product_to_cart_via_list("31/1/1")
    with allure.step("Set customer cookie"):
        browser.open("/Themes/DefaultClean/Content/images/logo.png")
        browser.driver.add_cookie({"name": "Nop.customer", "value": customer})
    with allure.step("Check cart counter"):
        browser.open("")
        browser.element(".cart-qty").should(have.text("1"))


def test_verify_cart_clearing():
    with allure.step("Add product to cart"):
        customer = cart.add_product_to_cart_via_list("31/1/1")
    with allure.step("Set customer cookie"):
        browser.open("/Themes/DefaultClean/Content/images/logo.png")
        browser.driver.add_cookie({"name": "Nop.customer", "value": customer})
    with allure.step("Clear cart"):
        browser.open("/cart")
        browser.element(".remove-from-cart input").click()
        browser.element(".update-cart-button").click()
    with allure.step("Check cart is empty"):
        browser.element(".order-summary-content").should(
            have.text("Your Shopping Cart is empty!")
        )


def test_verify_cart_deleting_item():
    with allure.step("Add products to cart"):
        customer = cart.add_product_to_cart_via_list("31/1/1")
        cart.add_product_to_cart_via_list("/36/1/1", customer)
    with allure.step("Set customer cookie"):
        browser.open("/Themes/DefaultClean/Content/images/logo.png")
        browser.driver.add_cookie({"name": "Nop.customer", "value": customer})
    with allure.step("Check items qty before deleting"):
        browser.open("/cart")
        assert len(browser.elements(".cart-item-row")) == 2
    with allure.step("Delete one item"):
        browser.elements(".remove-from-cart").first.click()
        browser.element(".update-cart-button").click()
    with allure.step("Check item list has changed"):
        assert len(browser.elements(".cart-item-row")) == 1


def test_verify_changing_qty():
    with allure.step("Add products to cart"):
        customer = cart.add_product_to_cart_via_list("14/1/1")
    with allure.step("Set customer cookie"):
        browser.open("/Themes/DefaultClean/Content/images/logo.png")
        browser.driver.add_cookie({"name": "Nop.customer", "value": customer})
    with allure.step("Update item qty"):
        browser.open("/cart")
        browser.element(".qty-input").click().set("2")
        browser.element(".update-cart-button").click()
    with allure.step("Check item qty has changed"):
        browser.open("/cart")
        browser.element(".qty-input").should(have.value("2"))
