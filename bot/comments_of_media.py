import json
from .urls import url_graphql_media_comments

def get_comments_of_media(self, code):
    comments = []
    if self.login_status:
        url = url_graphql_media_comments % (code,'')
        try:
            r = self.s.get(url)
            all_data = json.loads(r.text)            
            has_next_page = all_data['data']['shortcode_media']['edge_media_to_comment']['page_info']['has_next_page']
            comments = list(
                all_data['data']['shortcode_media']['edge_media_to_comment']['edges'])

            while(has_next_page):
                end_cursor = all_data['data']['shortcode_media']['edge_media_to_comment']['page_info']['end_cursor']
                url = url_graphql_media_comments % (code, end_cursor)
                r = self.s.get(url)
                all_data = json.loads(r.text)
                comments.extend(list(
                    all_data['data']['shortcode_media']['edge_media_to_comment']['edges'])
                )
                has_next_page = all_data['data']['shortcode_media']['edge_media_to_comment']['page_info']['has_next_page']

            # TODO: check ignore account for owner and comments
        except:
            comments = []
    return comments