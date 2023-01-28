from model import api
from requests import Response


def test_get_users_list():
    response: Response = api.test_session.get()
