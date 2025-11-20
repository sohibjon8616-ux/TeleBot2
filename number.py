from telebot import TeleBot,types

token = "8542688855:AAFS0sA5ioIZpXc98f-Q_5NfUdEmnh9SYMo"
bot = TeleBot(token)

@bot.message_handler(commands=['start',"boshla"])
def start(message):
    bot.send_message(message.chat.id, "Biror raqam kiriting va shu raqamni juft yoki toqligini bilib oling")

@bot.message_handler(func=lambda message:True)
def send(message):
    try:
        raqam = int(message.text)
        if raqam % 2 == 0:
            bot.send_message(message.chat.id, "Juft son yozdingiz")
        elif raqam % 2 == 1:
            bot.send_message(message.chat.id, "Toq son yozdingiz")
        else:
            bot.send_message(message.chat.id, "Xato malumot iltimos raqam kiriting")
    except:
        bot.send_message(message.chat.id, "Xato malumot iltimos raqam kiriting")
        
print("Dastur ishga tushdi")
bot.infinity_polling()
