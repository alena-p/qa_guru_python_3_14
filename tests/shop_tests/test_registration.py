from time import sleep

import allure
from mimesis.enums import Locale, Gender
from selene import have

from model import user
from selene.support.shared import browser
from mimesis import Person


def test_successful_registration():
    with allure.step("Prepare test data"):
        person = Person(Locale.EN)
        registration_data = {
            "Gender": "M",
            "FirstName": person.first_name(gender=Gender.MALE),
            "LastName": person.last_name(gender=Gender.MALE),
            "Email": person.email(),
            "Password": "123456",
            "ConfirmPassword": "123456",
            "register-button": "Register",
        }
    with allure.step("User registration"):
        auth_cookies = user.registration(registration_data)
    with allure.step("Set customer cookie"):
        browser.open("/Themes/DefaultClean/Content/images/logo.png")
        browser.driver.add_cookie(
            {"name": "NOPCOMMERCE.AUTH", "value": auth_cookies["NOPCOMMERCE.AUTH"]}
        )
    with allure.step("Check successful registration"):
        browser.open("")
        sleep(5)
        browser.element(".account").should(have.text(registration_data["Email"]))


def test_successful_authorization():
    with allure.step("Prepare test data"):
        email = "jylunecyk@mailinator.com"
        password = "123456"
    with allure.step("User authorization"):
        auth_cookies = user.authorization(email, password)
    with allure.step("Set customer cookie"):
        browser.open("/Themes/DefaultClean/Content/images/logo.png")
        browser.driver.add_cookie(
            {"name": "NOPCOMMERCE.AUTH", "value": auth_cookies["NOPCOMMERCE.AUTH"]}
        )
    with allure.step("Check successful authorization"):
        browser.open("")
        browser.element(".account").should(have.text(email))
