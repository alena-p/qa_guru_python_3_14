from dataclasses import dataclass


@dataclass
class Hosts:
    def __init__(self, env):
        self.shop = {
            "stage": "https://stage-demowebshop.tricentis.com",
            "prod": "https://demowebshop.tricentis.com",
        }[env]
        self.reqres = {
            "stage": "https://stage-reqres.in",
            "prod": "https://reqres.in/api",
        }[env]
