import telebot
from screen_url import Screen
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
TOKEN = config["Telegram"]["TOKEN"]


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def started(message):
    bot.send_message(message.from_user.id, 'Пришлите мне ссылку и я сделаю скрин страницы.')


@bot.message_handler(content_types=['text'])
def get_message(message):
    user_id = message.from_user.id
    if message.text:
        bot.send_message(user_id, 'Скоро все будет готово.')
        go = Screen(message.text, user_id)
        png_ = go.returnAnsver
        if png_['err']:
            bot.send_message(user_id, 'Не удалось сделать скрин.')
        else:
            bot.send_photo(user_id, photo=open(png_['screen'], 'rb'))

if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)