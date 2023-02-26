from model import api


def authorization(data):
    response = api.shop_session.post(
        url="/login",
        json=data,
        allow_redirects=False,
    )
    cookies = {
        "Nop.customer": response.cookies.get("Nop.customer"),
        "NOPCOMMERCE.AUTH": response.cookies.get("NOPCOMMERCE.AUTH"),
    }
    return cookies
