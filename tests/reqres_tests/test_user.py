from mimesis.enums import Locale, Gender

from model import api
from requests import Response
from mimesis import Person


def test_create_user():
    person = Person(Locale.EN)
    new_user_data = {
        "name": person.first_name(gender=Gender.MALE),
        "job": person.occupation(),
    }

    response: Response = api.reqres_session.post(url="/users", data=new_user_data)

    assert response.status_code == 201
    assert response.json()["name"] == new_user_data["name"]
    assert response.json()["job"] == new_user_data["job"]
    assert response.json()["id"]


def test_update_user():
    person = Person(Locale.EN)
    new_user_data = {
        "name": person.first_name(gender=Gender.MALE),
        "job": person.occupation(),
    }

    response: Response = api.reqres_session.put(url="/users/2", data=new_user_data)

    assert response.status_code == 200
    assert response.json()["name"] == new_user_data["name"]
    assert response.json()["job"] == new_user_data["job"]


def test_get_unexisting_page_users_list():
    response_first: Response = api.reqres_session.get(
        url="/users", params={"per_page": 20, "page": 1}
    )
    maximum_pages = response_first.json()["total_pages"]

    response_second: Response = api.reqres_session.get(
        url="/users", params={"per_page": 20, "page": maximum_pages + 1}
    )

    assert response_second.status_code == 200
    assert len(response_second.json()["data"]) == 0
