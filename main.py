import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise ValueError("❌ BOT_TOKEN is not set!")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📈 Get Signals", callback_data="signals")],
        [InlineKeyboardButton("💎 Premium Access", callback_data="premium")],
        [InlineKeyboardButton("📞 Contact Support", callback_data="contact")],
        [InlineKeyboardButton("⚠️ Disclaimer", callback_data="disclaimer")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "📊 *VEXO – Crash Signals*\n\nSmart probability-based crash signals.\nChoose an option below 👇",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "signals":
        await query.edit_message_text("📈 *Crash Signals*\n\nSignals are shared in our private channel.\nPremium users get early access 🚀", parse_mode="Markdown")
    elif query.data == "premium":
        await query.edit_message_text("💎 *Premium Access*\n\nPrice: Rs.250 / month\n\n💳 Payment Methods:\n• eZ Cash\n• Bank Transfer\n\nAfter payment, contact support.", parse_mode="Markdown")
    elif query.data == "contact":
        await query.edit_message_text("📞 *Contact Support*\n\nTelegram: @VexoSupport\nResponse time: < 24 hours", parse_mode="Markdown")
    elif query.data == "disclaimer":
        await query.edit_message_text("⚠️ *Disclaimer*\n\nAll signals are probability-based.\nNo guaranteed profits.\nPlay responsibly.", parse_mode="Markdown")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(menu_handler))
    print("Bot is starting... 🚀")
    app.run_polling()

if __name__ == "__main__":
    main()
