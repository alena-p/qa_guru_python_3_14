import os
import pytest
from dotenv import load_dotenv
from tests.conftest import env
from utils.base_session import BaseSession
from config import Hosts

# load_dotenv()
#
# reqres_api_url = os.getenv("REQRES_API_URL")
# shop_api_url = os.getenv("SHOP_API_URL")
#
#
# reqres_session = BaseSession(base_url=reqres_api_url)
# shop_session = BaseSession(base_url=shop_api_url)


reqres_session = BaseSession(base_url=Hosts(env).reqres)
shop_session = BaseSession(base_url=Hosts(env).shop)
