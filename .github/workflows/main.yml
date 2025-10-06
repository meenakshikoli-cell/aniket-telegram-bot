import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# अपना Telegram Bot Token डालो
TOKEN = "8299075637:AAG-UojJr48lhCD9H3N2CBPhRP5hXOP4un8"

# अपना OpenAI API Key डालो (https://platform.openai.com/account/api-keys से लो)
OPENAI_API_KEY = "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"

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    # OpenAI API पर रिक्वेस्ट
    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}"}
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": user_text}]
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", json=data, headers=headers)
    
    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
    else:
        reply = "माफ करना, कुछ गड़बड़ हो गई है। 😅"

    await update.message.reply_text(reply)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
app.run_polling()
