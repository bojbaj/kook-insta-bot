import json
from .urls import url_tag


def get_media_id_by_tag(self, tag):

    self.media_by_tag = []
    if self.login_status:
        url = url_tag % (tag)
        try:
            r = self.s.get(url)
            all_data = json.loads(r.text)
            self.media_by_tag = list(all_data['graphql']['hashtag']['edge_hashtag_to_media']['edges'])
        except:
            self.media_by_tag = []                    
    return self.media_by_tag
