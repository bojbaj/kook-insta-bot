import json
from .urls import url_unlike


def unlike(self, media_id):
    if self.login_status:
        url = url_unlike % (media_id)
        try:
            unlike = self.s.post(url)
            if unlike.status_code == 200:
                return True, 'ok'
        except Exception, e:
            return False, str(e)
    return False, 'fail'
