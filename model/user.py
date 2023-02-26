from model import api


def registration(data):
    init_reg_response = api.shop_session.get(url="/register")
    registration_token = init_reg_response.cookies.get("__RequestVerificationToken")
    data["__RequestVerificationToken"] = registration_token
    post_reg_response = api.shop_session.post(
        url="/register",
        json=data,
        allow_redirects=False,
    )
    result_reg_response = api.shop_session.get(url="/registerresult/1")
    cookies = {
        "Nop.customer": result_reg_response.cookies.get("Nop.customer"),
        "NOPCOMMERCE.AUTH": result_reg_response.cookies.get("NOPCOMMERCE.AUTH"),
    }
    return cookies


def authorization(email, password):
    response = api.shop_session.post(
        "/login", json={"Email": email, "Password": password}, allow_redirects=False
    )
    cookies = {
        "Nop.customer": response.cookies.get("Nop.customer"),
        "NOPCOMMERCE.AUTH": response.cookies.get("NOPCOMMERCE.AUTH"),
    }
    return cookies
