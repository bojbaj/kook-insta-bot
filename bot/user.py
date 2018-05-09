import json
import requests
import re

class UserInfo:
    user_agent = ("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36")
    url_user_info = "https://www.instagram.com/%s/"
    url_list = {
        "ink361": {
            "main": "http://ink361.com/",
            "user": "http://ink361.com/app/users/%s",
            "search_name": "https://data.ink361.com/v1/users/search?q=%s",
            "search_id": "https://data.ink361.com/v1/users/ig-%s",
            "followers": "https://data.ink361.com/v1/users/ig-%s/followed-by",
            "following": "https://data.ink361.com/v1/users/ig-%s/follows",
            "stat": "http://ink361.com/app/users/ig-%s/%s/stats"
        }
    }

    def __init__(self, info_aggregator="ink361"):
        self.i_a = info_aggregator
        self.hello()

    def hello(self):
        self.s = requests.Session()
        self.s.headers.update({'User-Agent': self.user_agent})
        main = self.s.get(self.url_list[self.i_a]["main"])
        if main.status_code == 200:
            return True
        return False

    def get_user_id_by_login(self, user_name):
        url_info = self.url_user_info % (user_name)
        info = self.s.get(url_info)
        json_info = json.loads(re.search('{"activity.+show_app', info.text, re.DOTALL).group(0)+'":""}')
        id_user = json_info['entry_data']['ProfilePage'][0]['graphql']['user']['id']
        return id_user