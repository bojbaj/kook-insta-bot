import requests
import time
import random
from .login import login, reload_session, is_logged_in
from .db import DB
from .media_by_tag import get_media_id_by_tag


class InstaBot:
    """
    Instagram bot
    https://github.com/-----
    """

    # request config
    user_agent = "" ""
    accept_language = 'en-US,en;q=0.5'

    def __init__(self, user_name=None, password=None, user_id=None):
        self.user_login = user_name
        self.user_password = password
        self.user_id = user_id
        self.csrftoken = None
        self.s = requests.Session()
        if(self.user_id != None):
            self.reload_session()

    def reload_session(self):
        return reload_session(self)

    def is_logged_in(self, ):
        self.login_status, self.csrftoken, self.user_id = is_logged_in(self)
        return self.login_status, self.csrftoken, self.user_id

    def login(self):
        self.login_status, self.csrftoken, self.user_id = login(self)
        return self.login_status, self.csrftoken, self.user_id

    def set_insta_target(self, target_hashtags, ignore_hashtags,
                         target_accounts, ignore_accounts):
        self.db = DB()
        return self.db.set_insta_target(self.user_id, target_hashtags, ignore_hashtags,
                                        target_accounts, ignore_accounts)

    def get_media_id_by_tag(self, tag):
        return get_media_id_by_tag(self, tag)
