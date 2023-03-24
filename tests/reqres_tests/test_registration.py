from pytest_voluptuous import S
import allure
from model import api
from mimesis.enums import Locale
from mimesis import Person
from schemas.registration import output


def test_successful_registration(env):
    with allure.step("Get user"):
        person = Person(Locale.EN)
        response_users_list = api.Reqres(env).users_list(
            params={"per_page": 1, "page": 1}
        )
        defined_user = response_users_list.json()["data"][0]
        registration_data = {
            "email": defined_user["email"],
            "password": person.password(),
        }
    with allure.step("Register user"):
        response_registration = api.Reqres(env).registration(registration_data)
    with allure.step("Check response is successful"):
        assert response_registration.status_code == 200
        assert S(output) == response_registration.json()


def test_unsuccessful_registration(env):
    with allure.step("Prepare test data"):
        person = Person(Locale.EN)
        registration_data = {"email": person.email()}
    with allure.step("Register user"):
        response = api.Reqres(env).registration(registration_data)
    with allure.step("Check response is unsuccessful"):
        assert response.status_code == 400
        assert response.json()["error"] == "Missing password"
