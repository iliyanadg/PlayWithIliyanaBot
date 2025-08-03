from flask import Flask
from threading import Thread
import telebot
from telebot import types

# === Web server per tenerlo attivo ===
app = Flask('')

import datetime

@app.route('/')
def home():
    now = datetime.datetime.now()
    print(f"Ping ricevuto: {now}")
    return "Bot attivo"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Avvia il web server
keep_alive()

# === Bot Telegram ===
API_TOKEN = '8113245535:AAEm0k2TRVxeki8whpI1ePJwcFz1rYA5Wco'  # Token del bot
ADMIN_USER_ID = 7144033450  # Il tuo ID personale (Iliyana)

bot = telebot.TeleBot(API_TOKEN)

# Messaggio di benvenuto quando l’utente avvia la chat con il bot
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Ciao 😘\n\n"
        "Io sono il *PlayBot di Iliyana* 💖\n"
        "Se vuoi scoprire quanto può essere *provocante*, scrivile una domanda qui sotto 💌\n\n"
        "⚠️ *Ma attenzione:* Le risposte te le scrive *davvero lei*, nel gruppo.\n"
        "Io servo solo per farti restare *anonimo* 😏\n\n"
        "*Non trattenerti* 😈",
        parse_mode='Markdown'
    )

# Quando un utente scrive in privato al bot
@bot.message_handler(func=lambda message: message.chat.type == "private")
def handle_private_message(message):
    user = message.from_user
    text = message.text

    # Inoltra la domanda a Iliyana
    bot.send_message(ADMIN_USER_ID, f"📩 Nuova domanda da {user.first_name}:\n\n{text}")

    # Risposta automatica all’utente con link OnlyFans
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("🔥 Vai su OnlyFans", url="https://onlyfans.com/iliyanadg")
    markup.add(button)

    bot.send_message(
        message.chat.id,
        "💋 La tua domanda è stata recapitata a Iliyana.\n"
        "Preparati a ricevere una risposta *calda* da parte sua nel gruppo, in perfetto anonimato... 😈\n\n"
        "Non riesci ad aspettare?\nScoprimi *davvero* su OnlyFans cliccando qui sotto 💦",
        reply_markup=markup,
        parse_mode='Markdown'
    )

# Avvia il bot
bot.polling()




