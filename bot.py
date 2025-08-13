from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    ChatMemberHandler,
    ChatJoinRequestHandler
)
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = 'TOKEN'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('ربات فعال است و آماده تایید درخواست‌های عضویت!')

async def approve_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.chat_join_request.approve()
        user = update.chat_join_request.from_user
        chat = update.chat_join_request.chat
        logger.info(f"درخواست عضویت {user.full_name} در {chat.title} تایید شد.")
    except Exception as e:
        logger.error(f"خطا در تایید عضویت: {e}")

async def track_chats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    old_status = update.my_chat_member.old_chat_member.status
    new_status = update.my_chat_member.new_chat_member.status
    
    if old_status == "left" and new_status in ["member", "administrator", "creator"]:
        logger.info(f"ربات به {update.my_chat_member.chat.title} اضافه شد!")
    elif old_status in ["member", "administrator", "creator"] and new_status == "left":
        logger.info(f"ربات از {update.my_chat_member.chat.title} حذف شد!")

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(ChatJoinRequestHandler(approve_join_request))
    application.add_handler(ChatMemberHandler(track_chats, ChatMemberHandler.MY_CHAT_MEMBER))
    
    application.run_polling()

if __name__ == '__main__':
    main()