# Instagram Urls
url = 'https://www.instagram.com/'
url_tag = 'https://www.instagram.com/explore/tags/%s/?__a=1&max_id='
url_likes = 'https://www.instagram.com/web/likes/%s/like/'
url_unlike = 'https://www.instagram.com/web/likes/%s/unlike/'
url_comment = 'https://www.instagram.com/web/comments/%s/add/'
url_follow = 'https://www.instagram.com/web/friendships/%s/follow/'
url_unfollow = 'https://www.instagram.com/web/friendships/%s/unfollow/'
url_login = 'https://www.instagram.com/accounts/login/ajax/'
url_logout = 'https://www.instagram.com/accounts/logout/'
url_media_detail = 'https://www.instagram.com/p/%s/?__a=1'
url_user_detail = 'https://www.instagram.com/%s/'
api_user_detail = 'https://i.instagram.com/api/v1/users/%s/info/'
url_search = 'https://www.instagram.com/web/search/topsearch/?query=%s'

# GraphQL
url_graphql_media_likes ='https://www.instagram.com/graphql/query/?query_id=17864450716183058&variables={"shortcode":"%s","first":50,"after":"%s"}'
url_graphql_media_comments ='https://www.instagram.com/graphql/query/?query_id=17852405266163336&variables={"shortcode":"%s","first":50,"after":"%s"}'
url_graphql_account_medias = 'https://www.instagram.com/graphql/query/?query_hash=42323d64886122307be10013ad2dcc44&variables={"id": %s, "first": 50, "after": "%s"}'
url_graphql_account_medias_alt  = 'https://www.instagram.com/graphql/query/?query_id=17880160963012870&id={{accountId}}&first=10&after='
url_graphql_following = 'https://www.instagram.com/graphql/query/?query_id=17874545323001329&id=%s&first=50&after=%s'
url_graphql_follower = 'https://www.instagram.com/graphql/query/?query_id=17851374694183129&id=%s&first=50&after=%s'
url_graphql_recent_feed = 'https://www.instagram.com/graphql/query/?query_id=17861995474116400&fetch_media_item_count=12&fetch_media_item_cursor=&fetch_comment_count=4&fetch_like=10'
url_graphql_user_info = 'https://i.instagram.com/api/v1/users/%s/info/' #user_id