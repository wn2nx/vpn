import telebot

# هشدار: توکن ربات خود را به صورت عمومی به اشتراک نگذارید
# این توکن باید محرمانه بماند.
BOT_TOKEN = '8203812802:AAHf6qzWHlIPFws51lrUqkWVjth1_w9qTxA'

# شناسه کاربری شما
YOUR_CHAT_ID = 1299749738

# ساخت یک نمونه از ربات
bot = telebot.TeleBot(BOT_TOKEN)

# یک هندلر برای دستور /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # بررسی کنید که آیا دستور از طرف شما ارسال شده است
    if message.chat.id == YOUR_CHAT_ID:
        # ارسال پاسخ "سلام"
        bot.send_message(message.chat.id, "سلام")
    else:
        # اگر از طرف شخص دیگری باشد، یک پاسخ متفاوت ارسال می‌شود
        bot.send_message(message.chat.id, "شما اجازه دسترسی به این ربات را ندارید.")

# اجرای ربات
bot.polling()
