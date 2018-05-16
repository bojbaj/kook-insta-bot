import json
from .urls import url_unfollow


def unfollow(self, user_id):
    if self.login_status:
        url = url_unfollow % (user_id)
        try:
            print(url)
            unfollow = self.s.post(url)
            print(unfollow.text)
            if unfollow.status_code == 200:                
                return True, 'ok'
        except Exception, e:
            return False, str(e)
        return False, 'fail'
