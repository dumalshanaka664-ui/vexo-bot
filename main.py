import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

import os
TOKEN = os.environ["8100433887:AAE_FxEm5gVky7QXi6PGQzyR08C0rto-L7M"]
print("8100433887:AAE_FxEm5gVky7QXi6PGQzyR08C0rto-L7M", TOKEN[:5], "...")  # optional: check if Railway loaded it


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📈 Get Signals", callback_data="signals")],
        [InlineKeyboardButton("💎 Premium Access", callback_data="premium")],
        [InlineKeyboardButton("📞 Contact Support", callback_data="contact")],
        [InlineKeyboardButton("⚠️ Disclaimer", callback_data="disclaimer")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "📊 *VEXO – Crash Signals*\n\n"
        "Smart probability-based crash signals.\n"
        "Choose an option below 👇",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "signals":
        await query.edit_message_text(
            "📈 *Crash Signals*\n\n"
            "Signals are shared in our private channel.\n"
            "Premium users get early access 🚀",
            parse_mode="Markdown"
        )

    elif query.data == "premium":
        await query.edit_message_text(
            "💎 *Premium Access*\n\n"
            "Price: $10 / month\n\n"
            "💳 Payment Methods:\n"
            "• USDT (TRC20)\n"
            "• Binance Pay\n\n"
            "After payment, contact support.",
            parse_mode="Markdown"
        )

    elif query.data == "contact":
        await query.edit_message_text(
            "📞 *Contact Support*\n\n"
            "Telegram: @VexoSupport\n"
            "Response time: < 24 hours",
            parse_mode="Markdown"
        )

    elif query.data == "disclaimer":
        await query.edit_message_text(
            "⚠️ *Disclaimer*\n\n"
            "All signals are probability-based.\n"
            "No guaranteed profits.\n"
            "Play responsibly.",
            parse_mode="Markdown"
        )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(menu_handler))
    app.run_polling()

if __name__ == "__main__":
    main()

