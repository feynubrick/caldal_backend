import os

from dotenv import load_dotenv

from .base import *

load_dotenv()

SECRET_KEY = os.environ["SECRET_KEY"]
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
