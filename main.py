import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import random

# ------------------- TOKEN -------------------
TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise ValueError("❌ BOT_TOKEN environment variable is missing!")

# ------------------- START MENU -------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📈 Get Signals", callback_data="signals")],
        [InlineKeyboardButton("💎 Premium Access", callback_data="premium")],
        [InlineKeyboardButton("🎮 Play Crash Game", callback_data="crash")],
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

# ------------------- MENU HANDLER -------------------
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
            "Price: Rs.250 / month\n\n"
            "💳 Payment Methods:\n"
            "• eZ Cash\n"
            "• Bank Transfer\n\n"
            "After payment, contact support.",
            parse_mode="Markdown"
        )

    elif query.data == "crash":
        # Simulate a crash multiplier
        multiplier = round(random.uniform(1.0, 10.0), 2)
        await query.edit_message_text(
            f"🎮 *Crash Game*\n\n"
            f"Your round multiplier: *{multiplier}x*\n\n"
            "💡 Click /start to play again or choose another menu option.",
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
            "All signals and crash results are probability-based.\n"
            "No guaranteed profits.\n"
            "Play responsibly.",
            parse_mode="Markdown"
        )

# ------------------- MAIN -------------------
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(menu_handler))

    print("🚀 Bot is starting...")
    app.run_polling()

if __name__ == "__main__":
    main()
