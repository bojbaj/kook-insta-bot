from .urls import url_like


def like(self, media_id):
    if self.login_status:
        url = url_like % (media_id)
        try:
            like = self.s.post(url)
            if like.status_code == 200:
                return True, 'ok'
        except Exception, e:
            return False, str(e)
    return False, 'fail'
