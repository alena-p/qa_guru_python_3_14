from pytest_voluptuous import S
import allure
from model import api
from requests import Response
from mimesis.enums import Locale
from mimesis import Person
from schemas.registration import output


def test_successful_registration():
    with allure.step("Get user"):
        person = Person(Locale.EN)
        response_users_list: Response = api.reqres_session.get(
            url="/users", params={"per_page": 1, "page": 1}
        )
        defined_user = response_users_list.json()["data"][0]
        registration_data = {
            "email": defined_user["email"],
            "password": person.password(),
        }
    with allure.step("Register user"):
        response_registration: Response = api.reqres_session.post(
            url="/register", data=registration_data
        )
    with allure.step("Check response is successful"):
        assert response_registration.status_code == 200
        assert S(output) == response_registration.json()


def test_unsuccessful_registration():
    with allure.step("Prepare test data"):
        person = Person(Locale.EN)
        registration_data = {"email": person.email()}
    with allure.step("Register user"):
        response: Response = api.reqres_session.post(
            url="/register", data=registration_data
        )
    with allure.step("Check response is unsuccessful"):
        assert response.status_code == 400
        assert response.json()["error"] == "Missing password"
