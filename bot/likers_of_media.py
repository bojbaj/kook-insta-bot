import json
from .urls import url_media_detail, url_media_detail_graphql, url_media_detail_graphql_more


def get_likers_of_media_legacy(self, code):
    likers = []
    if self.login_status:
        url = url_media_detail % (code)
        try:
            r = self.s.get(url)
            all_data = json.loads(r.text)
            likers = list(
                all_data['graphql']['shortcode_media']['edge_media_preview_like']['edges'])
            # TODO: check ignore account for owner and likers
        except:
            likers = []
    return likers


def get_likers_of_media_graphQL(self, code):
    likers = []
    if self.login_status:
        url = url_media_detail_graphql % (code)
        try:
            r = self.s.get(url)
            all_data = json.loads(r.text)

            has_next_page = all_data['data']['shortcode_media']['edge_liked_by']['page_info']['has_next_page']
            likers = list(
                all_data['data']['shortcode_media']['edge_liked_by']['edges'])

            while(has_next_page):
                end_cursor = all_data['data']['shortcode_media']['edge_liked_by']['page_info']['end_cursor']
                url = url_media_detail_graphql_more % (code, end_cursor)
                r = self.s.get(url)
                all_data = json.loads(r.text)
                likers.extend(list(
                    all_data['data']['shortcode_media']['edge_liked_by']['edges'])
                )
                has_next_page = all_data['data']['shortcode_media']['edge_liked_by']['page_info']['has_next_page']

            # TODO: check ignore account for owner and likers
        except:
            likers = []
    return likers
