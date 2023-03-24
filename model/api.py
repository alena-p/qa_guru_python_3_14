from utils.base_session import BaseSession
from config import Hosts


class Reqres:
    def __init__(self, env):
        self.reqres = BaseSession(base_url=Hosts(env).reqres)

    def users_list(self, params):
        response = self.reqres.get(url="/users", params=params)
        return response

    def registration(self, registration_data):
        response = self.reqres.post(url="/register", data=registration_data)
        return response

    def create_user(self, data):
        response = self.reqres.post(url="/users", data=data)
        return response

    def update_user(self, data):
        response = self.reqres.put(url="/users/2", data=data)
        return response


class Shop:
    def __init__(self, env):
        self.shop = BaseSession(base_url=Hosts(env).shop)

    def authorization(self, data):
        response = self.shop.post(
            url="/login",
            json=data,
            allow_redirects=False,
        )
        cookies = {
            "Nop.customer": response.cookies.get("Nop.customer"),
            "NOPCOMMERCE.AUTH": response.cookies.get("NOPCOMMERCE.AUTH"),
        }
        return cookies

    def add_product_to_cart_via_list(self, product, customer=""):
        headers = {"Cookie": f"Nop.customer={customer}"}
        response = self.shop.post(
            url=f"/addproducttocart/catalog/{product}", headers=headers
        )
        customer = response.cookies.get("Nop.customer")
        return customer
