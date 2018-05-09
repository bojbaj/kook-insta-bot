from bot import InstaBot

bot = InstaBot('kook.insta.bot.demo', 'kook123')
login_result = bot.login()
print (login_result)

logged_in = login_result[0]
if logged_in == True:
    bot.set_insta_target('sport', 'gym', '', '')    

