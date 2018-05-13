from bot import InstaBot
from db import set_insta_user, set_insta_target, set_insta_media_by_hashtag

import json
import random

# bot = InstaBot('kook.insta.bot.demo', 'kook123')
# login_status, csrftoken, user_id = bot.login()
# print (login_status, csrftoken, user_id)

bot = InstaBot('kook.insta.bot.demo', user_id='7710672032')
login_status, csrftoken, user_id = bot.is_logged_in()
print (login_status, csrftoken, user_id)

if(login_status):
    set_insta_user(csrftoken, user_id)

    # SET target hashtag for specific user
    set_insta_target(user_id, 'sport', 'gym', '', '')

    # GET list of medias from a hashtag
    hastag = 'justien'
    medias = bot.get_media_id_by_tag(hastag)
    # TODO: Filter medias with ignore hashtag
    if(len(medias) > 0):
        set_insta_media_by_hashtag(hastag, medias)

        # TODO: list of medias from an account
        # TODO: Filter medias with ignore account

        # get likers of media
        # for media in medias:
        media = medias[random.randint(0, len(medias) - 1)]
        # media = medias[-1]
        media_id = media['node']['id']
        media_code = media['node']['shortcode']
        print ('the shortcode is', media_code)
        likes = bot.get_likes_of_media(media_code)
        print (len(likes), 'likes for this code:', media_code)

        comments = bot.get_comments_of_media(media_code)
        print (len(comments), 'comments for this code:', media_code)
    else:
        print ('no Media!')
