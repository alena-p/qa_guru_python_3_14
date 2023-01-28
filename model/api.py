import os

from dotenv import load_dotenv
from utils.base_session import BaseSession

load_dotenv()
api_url = os.getenv("API_URL")


test_session = BaseSession(base_url=api_url)
