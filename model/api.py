import os

from dotenv import load_dotenv
from utils.base_session import BaseSession

load_dotenv()
reqres_api_url = os.getenv("REQRES_API_URL")
shop_api_url = os.getenv("SHOP_API_URL")


reqres_session = BaseSession(base_url=reqres_api_url)
shop_session = BaseSession(base_url=shop_api_url)
