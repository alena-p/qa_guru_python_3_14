import allure
from requests import Session


class BaseSession(Session):
    def __init__(self, **kwargs):
        self.base_url = kwargs.pop("base_url")
        super().__init__()

    def request(self, method, url, **kwargs):
        headers = {}
        if "headers" in kwargs:
            headers = kwargs.pop("headers")

        with allure.step(f"{method} {url}"):
            return super().request(
                method, url=f"{self.base_url}{url}", headers=headers, **kwargs
            )
