import json
from .urls import url_follow


def follow(self, user_id):
    if self.login_status:
        url = url_follow % (user_id)
        try:
            print(url)
            follow = self.s.post(url)
            print(follow.text)
            if follow.status_code == 200:
                response = json.loads(follow.text)
                return True, response['result']
        except Exception, e:
            return False, str(e)
        return False, 'fail'
