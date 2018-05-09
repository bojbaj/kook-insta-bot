from bot import InstaBot

bot = InstaBot('kook.insta.bot.demo', 'kook123')
a = bot.login()
print (a)

if a[0] == True:
    bot.setInstaTarget('sport', 'gym', '', '')    
