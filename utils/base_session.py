import json
import logging
import allure
from json import JSONDecodeError
from requests import Session, Response
from allure_commons.types import AttachmentType
from curlify import to_curl


def allure_logger(function):
    def wrapper(*args, **kwargs):
        method, url = args[1], args[2]
        with allure.step(f"{method} {url}"):
            response: Response = function(*args, **kwargs)
            allure.attach(
                body=to_curl(response.request).encode("utf8"),
                name=f"Request {response.status_code}",
                attachment_type=AttachmentType.TEXT,
                extension=".txt",
            )
            try:
                allure.attach(
                    body=json.dumps(response.json(), indent=4).encode("utf8"),
                    name=f"Response {response.status_code}",
                    attachment_type=AttachmentType.JSON,
                    extension=".json",
                )
            except JSONDecodeError:
                allure.attach(
                    body=response.text,
                    name=f"Response {response.status_code}",
                    attachment_type=AttachmentType.TEXT,
                    extension=".txt",
                )
        return response

    return wrapper


def console_logger(function):
    def wrapper(*args, **kwargs):
        response: Response = function(*args, **kwargs)
        logging.info(f"{response.status_code} {to_curl(response.request)}")

        return response

    return wrapper


class BaseSession(Session):
    def __init__(self, **kwargs):
        self.base_url = kwargs.pop("base_url")
        super().__init__()

    @allure_logger
    @console_logger
    def request(self, method, url, **kwargs):
        headers = {}
        if "headers" in kwargs:
            headers = kwargs.pop("headers")
        response = super().request(
            method, url=f"{self.base_url}{url}", headers=headers, **kwargs
        )
        return response
