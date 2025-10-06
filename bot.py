from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8299075637:AAG-UojJr48lhCD9H3N2CBPhRP5hXOP4un8"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("नमस्ते अनिकेत! 🤖 मैं तुम्हारा AI Bot हूँ।")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()