from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from config import Config
from translation import Translation 
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

bot = Cient(
  'simp',
  api_id = Config.API_ID,
  api_hash = Config.API_HASH,
  bot_token = Config.BOT_TOKEN
)

@bot.on_message(filters.command("start"))
def start(bot, message):
  Animes.send_message("Hi there")
  
@bot.on_message(filters.command("id"))
def get_id(bot, message):
  message.reply(f"Your id is {message.from_user.id} \nJoin @Animes_Encoded")
  
