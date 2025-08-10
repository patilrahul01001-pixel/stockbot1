import telebot
import time
import threading

# Hardcoded Bot Token & Chat ID
BOT_TOKEN = "8163501755:AAE4uvPp4Y4mSlR1kbWYYXWHSTJU5TyQCzo"
CHAT_ID = "-1096603305"

bot = telebot.TeleBot(BOT_TOKEN)

# Send stock suggestions
def send_weekly_message():
    while True:
        bot.send_message(CHAT_ID, "📊 Weekly Stock Suggestions:\n1. Stock A\n2. Stock B\n3. Stock C\n...\n10. Stock J")
        time.sleep(7 * 24 * 60 * 60)  # Wait 7 days

# Start the weekly message thread
threading.Thread(target=send_weekly_message, daemon=True).start()

# Keyboard buttons
@bot.message_handler(commands=["start"])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📈 Get Weekly Stocks", "💬 Send Command")
    bot.send_message(message.chat.id, "Welcome! Choose an option:", reply_markup=markup)

# Handle button presses
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "📈 Get Weekly Stocks":
        bot.send_message(message.chat.id, "📊 Today's Suggestions:\n1. Stock A\n2. Stock B\n...\n10. Stock J")
    elif message.text == "💬 Send Command":
        bot.send_message(message.chat.id, "Please type your command:")
    else:
        bot.send_message(message.chat.id, f"✅ Command received: {message.text}")

# Run bot
bot.polling(non_stop=True)
