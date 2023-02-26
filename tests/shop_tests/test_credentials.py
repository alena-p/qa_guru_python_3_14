import allure
from selene import have
from model import user
from selene.support.shared import browser


def test_successful_authorization():
    with allure.step("Prepare test data"):
        data = {"Email": "jylunecyk@mailinator.com", "Password": "123456"}
    with allure.step("User authorization"):
        auth_cookies = user.authorization(data)
    with allure.step("Set customer cookie"):
        browser.open("/Themes/DefaultClean/Content/images/logo.png")
        browser.driver.add_cookie(
            {"name": "NOPCOMMERCE.AUTH", "value": auth_cookies["NOPCOMMERCE.AUTH"]}
        )
    with allure.step("Check successful authorization"):
        browser.open("")
        browser.element(".account").should(have.text(data["Email"]))
