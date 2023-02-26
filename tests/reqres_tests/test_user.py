from mimesis.enums import Locale, Gender
import allure
from model import api
from requests import Response
from mimesis import Person


def test_create_user():
    with allure.step("Prepare test data"):
        person = Person(Locale.EN)
        new_user_data = {
            "name": person.first_name(gender=Gender.MALE),
            "job": person.occupation(),
        }
    with allure.step("Create user"):
        response: Response = api.reqres_session.post(url="/users", data=new_user_data)
    with allure.step("Check response is successful"):
        assert response.status_code == 201
        assert response.json()["name"] == new_user_data["name"]
        assert response.json()["job"] == new_user_data["job"]
        assert response.json()["id"]


def test_update_user():
    with allure.step("Prepare test data"):
        person = Person(Locale.EN)
        new_user_data = {
            "name": person.first_name(gender=Gender.MALE),
            "job": person.occupation(),
        }
    with allure.step("Update user"):
        response: Response = api.reqres_session.put(url="/users/2", data=new_user_data)
    with allure.step("Check response is successful"):
        assert response.status_code == 200
        assert response.json()["name"] == new_user_data["name"]
        assert response.json()["job"] == new_user_data["job"]


def test_get_unexisting_page_users_list():
    with allure.step("Get maximum page qty"):
        response_first: Response = api.reqres_session.get(
            url="/users", params={"per_page": 20, "page": 1}
        )
        maximum_pages = response_first.json()["total_pages"]
    with allure.step("Get page over range"):
        response_second: Response = api.reqres_session.get(
            url="/users", params={"per_page": 20, "page": maximum_pages + 1}
        )
    with allure.step("Check data is empty"):
        assert response_second.status_code == 200
        assert len(response_second.json()["data"]) == 0
