from pytest_voluptuous import S

from model import api
from requests import Response
from mimesis.enums import Locale
from mimesis import Person
from schemas.registration import output


def test_successful_registration():
    person = Person(Locale.EN)
    response_users_list: Response = api.test_session.get(
        url="/users", params={"per_page": 1, "page": 1}
    )
    defined_user = response_users_list.json()["data"][0]
    registration_data = {"email": defined_user["email"], "password": person.password()}

    response_registration: Response = api.test_session.post(
        url="/register", data=registration_data
    )

    assert response_registration.status_code == 200
    assert S(output) == response_registration.json()


def test_unsuccessful_registration():
    person = Person(Locale.EN)
    registration_data = {"email": person.email()}

    response: Response = api.test_session.post(url="/register", data=registration_data)

    assert response.status_code == 400
    assert response.json()["error"] == "Missing password"
