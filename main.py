from bot import InstaBot

bot = InstaBot('kook.insta.bot.demo', 'kook123')
login_result = bot.login()
print (login_result)
logged_in = login_result[0]

# bot = InstaBot('kook.insta.bot.demo', user_id='7710672032')
# login_result = bot.is_logged_in()
# print (login_result)
# logged_in = login_result[0]


# if logged_in == True:
#     bot.set_insta_target('sport', 'gym', '', '')
#     medias = bot.get_media_id_by_tag('sport')
#     print (medias)
