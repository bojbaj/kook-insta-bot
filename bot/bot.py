import requests
import time
import random
from .login import login

class InstaBot:
    """
    Instagram bot
    https://github.com/-----
    """

    # request config
    user_agent = "" ""
    accept_language = 'en-US,en;q=0.5'

    def __init__(self, user_name, password):
        self.user_login = user_name
        self.user_password = password
        self.s = requests.Session()

    def login(self):
        return login(self)
