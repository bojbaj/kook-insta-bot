import random
import time
from .urls import url, url_login
from .db import DB
from .user import UserInfo
import json
import requests
import requests.utils
import pickle


def login(self):
    self.db = DB()
    self.login_post = {
        'username': self.user_login,
        'password': self.user_password
    }

    self.s.headers.update({
        'Accept': '*/*',
        'Accept-Language': self.accept_language,
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Host': 'www.instagram.com',
        'Origin': 'https://www.instagram.com',
        'Referer': 'https://www.instagram.com/',
        'User-Agent': self.user_agent,
        'X-Instagram-AJAX': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Requested-With': 'XMLHttpRequest'
    })
    r = self.s.get(url)
    self.s.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
    time.sleep(1 * random.random())

    login = self.s.post(
        url_login, data=self.login_post, allow_redirects=True)
    self.s.headers.update({'X-CSRFToken': login.cookies['csrftoken']})
    self.csrftoken = login.cookies['csrftoken']
    # ig_vw=1536; ig_pr=1.25; ig_vh=772;  ig_or=landscape-primary;
    self.s.cookies['ig_vw'] = '1536'
    self.s.cookies['ig_pr'] = '1.25'
    self.s.cookies['ig_vh'] = '772'
    self.s.cookies['ig_or'] = 'landscape-primary'
    time.sleep(1 * random.random())

    if login.status_code == 200:
        r = self.s.get('https://www.instagram.com/')
        finder = r.text.find(self.user_login)
        if finder != -1:
            self.login_status = True
            ui = UserInfo()
            self.user_id = ui.get_user_id_by_login(self.user_login)
            self.db.set_insta_user(self.csrftoken, self.user_id)
            with open('cookies/cookie_' + self.user_id + '.ck', 'w') as f:
                pickle.dump(requests.utils.dict_from_cookiejar(
                    self.s.cookies), f)
        else:
            self.login_status = False
    else:
        self.login_status = False

    return self.login_status, self.csrftoken, self.user_id


def reload_session(self):   
    with open('cookies/cookie_' + self.user_id + '.ck') as f:
        cookies = requests.utils.cookiejar_from_dict(pickle.load(f))
        self.s.cookies = cookies

def is_logged_in(self):   
    # ig_vw=1536; ig_pr=1.25; ig_vh=772;  ig_or=landscape-primary;
    self.s.cookies['ig_vw'] = '1536'
    self.s.cookies['ig_pr'] = '1.25'
    self.s.cookies['ig_vh'] = '772'
    self.s.cookies['ig_or'] = 'landscape-primary'
    r = self.s.get('https://www.instagram.com/')
    finder = r.text.find(self.user_login)
    if finder != -1:
        self.login_status = True
        ui = UserInfo()
        self.csrftoken = r.cookies['csrftoken']        
        self.user_id = ui.get_user_id_by_login(self.user_login)
    else:
        self.login_status = False

    return self.login_status, self.csrftoken, self.user_id
