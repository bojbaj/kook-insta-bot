import random
import time
from .urls import url, url_login


def login(self):
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
    #ig_vw=1536; ig_pr=1.25; ig_vh=772;  ig_or=landscape-primary;
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
        else:
            self.login_status = False
    else:
        self.login_status = False

    return self.login_status, self.csrftoken
