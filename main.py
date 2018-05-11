from bot import InstaBot
import json
import random

# bot = InstaBot('kook.insta.bot.demo', 'kook123')
# login_result = bot.login()
# print (login_result)
# logged_in = login_result[0]

bot = InstaBot('kook.insta.bot.demo', user_id='7710672032')
login_result = bot.is_logged_in()
print (login_result)
logged_in = login_result[0]


if logged_in == True:
    # SET target hashtag for specific user
    # bot.set_insta_target('sport', 'gym', '', '')

    # GET list of medias from a hashtag
    medias = bot.get_media_id_by_tag('fun')
    print (len(medias), 'in fun')
    with open('tmp/medias.json', 'w') as f:
        f.writelines(json.dumps(medias, indent=4))

    # TODO: list of medias from an account
    # TODO: Filter medias with ignore hashtag
    # TODO: Filter medias with ignore account

    # get likers of media
    # for media in medias:
    if(len(medias) > 0):
        media = medias[random.randint(0, len(medias) - 1)]
        media_id = media['node']['id']
        media_code = media['node']['shortcode']
        print ('the shortcode is', media_code)
        liker = bot.get_likers_of_media(media_code)
        print (len(liker), 'for this code:', media_code)
        # with open('tmp/likers.json', 'w') as f:
        #     f.writelines(json.dumps(liker, indent=4))
    else:
        print ('no Media!')
