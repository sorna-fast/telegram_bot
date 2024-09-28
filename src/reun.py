import base
import telebot
import currency_convertor


base_currency=""


bot=telebot.TeleBot(base.token)

@bot.message_handler(commands=["strat","hello"])
def send_welcom(massege):
    #bot.send_message(massege.chat.id,"به ربات تبدیل خوش امدید")
    bot.reply_to(massege,"welcom to bot masud")

@bot.message_handler(commands=["link"])
def show_link(massege):


    first_Bouttion=telebot.types.InlineKeyboardButton("وبسایت w3",url="https://www.w3schools.com")
    secend_Bouttion=telebot.types.InlineKeyboardButton("fastapi",url="https://fastapi.tiangolo.com")
    markup=telebot.types.InlineKeyboardMarkup(row_width=1)
    markup.add(first_Bouttion,secend_Bouttion)
    bot.send_message(massege.chat.id,"یکی از لینک های زیر را انتخاب کنید",reply_markup = markup)


@bot.message_handler(commands=["help"])
def send_reply(massege):
    key_makup=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 =telebot.types.KeyboardButton("درباره ما")
    item2=telebot.types.KeyboardButton("تماس با ما ")
    item3=telebot.types.KeyboardButton("👈")
    key_makup.add(item1,item2,item3)
    bot.send_message(massege.chat.id,"یکی از موارد زیر را انتخاب کنید",reply_markup=key_makup)

@bot.message_handler(commands=["help"])
def send_reply(massege):
    key_makup=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 =telebot.types.KeyboardButton(" شیش ماهه")
    item2=telebot.types.KeyboardButton("چهار ماهه ")
    item3=telebot.types.KeyboardButton("👈")
    key_makup.add(item1,item2,item3)
    bot.send_message(massege.chat.id,"نوع عوضیت خود را انتخاب کنید",reply_markup=key_makup)


@bot.message_handler(func=lambda massage:True)
def handle_other_massage(massage):
    if massage.text == "درباره ما":
        bot.send_message(massage.chat.id,"گروخ توسظ کلاه سفید طراحی شده")
    elif massage.text == "تماس با ما":
        mail_info="currency@gmail.com"
        website="currency.com"
        phone="02133253"
        contac_info=f"ایمیل:{mail_info}\n وبسایت:{website},\n شماره تماس:{phone}"
        bot.send_message(massage.chat.id,contac_info)
    
    elif massage.text == "شیش ماهه":
        bot.send_message(massage.chat.id,"شما عضویت شیش ماهه انتخاب کردید")
    
    elif massage.text == "یک ساله":
        bot.send_message(massage.chat.id,"شما عضویت یک ساله انتخاب کردید")
    elif massage.text == "👈":
        markup=telebot.types.ReplyKeyboardRemove(selective=False)
        bot.send_message(massage.chat.id,"شما به منوی اصلی برگشتید",reply_markup=markup)
    
    else:
        bot.send_message(massage.chat.id,"منظور شما را متوجه نشدم")

@bot.message_handler(commands=["convert"])
def show_rate(messge):
    msg=bot.send_message(messge.chat.id,"لطفا ارز مورد نظر را انتنخاب کنید")
    bot.register_next_step_handler(msg,process_basecurrency_step)

def process_basecurrency_step(message):
    
    global base_currency
    base_currency=message.text.upper()

    msg=bot.reply_to(message,"لطفا ارز مقصد را انتخاب کنید")


if __name__=="__main__":
    #bot.polling()
    bot.infinity_polling()

