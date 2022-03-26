#библиотеки, которые загружаем из вне
import telebot
TOKEN = '!!!ВСТАВИТЬ СВОЙ ТОКЕН!!!'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🗂Дай в репу!")
	item2 = types.KeyboardButton("😏Шепни на ушко)")
	item3 = types.KeyboardButton("📬Для любителей голубей🕊")
	item4 = types.KeyboardButton("😎Чекни CV")

	markup.add(item1, item2, item3, item4)

	bot.send_message(message.chat.id, "Дороу! Как оно, {0.first_name}?))0)".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '🗂Дай в репу!':
			bot.send_message(message.chat.id, 'https://github.com/EvgenDar')
		elif message.text == '😏Шепни на ушко)':
			bot.send_message(message.chat.id, 'https://t.me/g_e_gg')
		elif message.text == '📬Для любителей голубей🕊':
			bot.send_message(message.chat.id, 'kreml1994@gmail.com')
		elif message.text == '😎Чекни CV':
			bot.send_message(message.chat.id, 'http://evgeniydarovskikh.ru/')
		else:
			bot.send_message(message.chat.id, 'Не знаю что ответить😢')


bot.polling(none_stop=True)
