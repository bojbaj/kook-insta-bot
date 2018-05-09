import requests
import time
import random
from .login import login
from .db import DB


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
        self.login_status, self.csrftoken, self.user_id = login(self)
        return self.login_status, self.csrftoken, self.user_id

    def setInstaTarget(self, target_hashtags, ignore_hashtags,
                       target_accounts, ignore_accounts):
        self.db = DB()
        return self.db.setInstaTarget(self.user_id, target_hashtags, ignore_hashtags,
                                      target_accounts, ignore_accounts)
