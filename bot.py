import telebot

with open("./bot.token", "r") as TOKEN:
    bot = telebot.TeleBot(TOKEN.readline())

@bot.message_handler(commands=["id"])
def id(m):
    user = m.from_user.id
    chat = m.chat.id
    bot.send_message(m.chat.id, "User: {}\nChat: {}".format(user, chat))

bot.skip_pending = True

print("Running...")
bot.polling()
