from model import api


def add_product_to_cart_via_list(product, customer=""):
    headers = {"Cookie": f"Nop.customer={customer}"}
    response = api.shop_session.post(
        url=f"/addproducttocart/catalog/{product}", headers=headers
    )
    customer = response.cookies.get("Nop.customer")
    return customer
