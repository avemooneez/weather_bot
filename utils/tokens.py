import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
bot_token = os.getenv('BOT_TOKEN')