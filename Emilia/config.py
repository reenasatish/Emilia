import json
import os


def get_user_list(config, key):
    with open("{}/Emilia/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    API_HASH = "4f6d1b67cf101aea5cf0536885aa1b82" # API_HASH from my.telegram.org
    API_ID = 27322718 # API_ID from my.telegram.org

    BOT_ID = 7572317246 # BOT_ID
    BOT_USERNAME = "seishiroxrenamerbot" # BOT_USERNAME

    MONGO_DB_URL = "mongodb+srv://seishiroatanime:Y3FQIzJbCXMWQc9S@cluster0.ymttr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0" # MongoDB URL from MongoDB Atlas

    SUPPORT_CHAT = "Seishiro_anime_chat" # Support Chat Username
    UPDATE_CHANNEL = "seishiro_atanime" # Update Channel Username
    START_PIC = "https://ibb.co/DH3N4Lyr" # Start Image
    DEV_USERS = [6040984893, 6461051572, 7107018652] # Dev Users
    TOKEN = "7572317246:AAH1NDpYS4illUWyWSRlRwIUvwEwhEDHlBo" # Bot Token from @BotFather
    CLONE_LIMIT = 0 # Number of clones your bot can make

    EVENT_LOGS = -1002369506236 # Event Logs Chat ID
    OWNER_ID = 6701907262 # Owner ID
 
    TEMP_DOWNLOAD_DIRECTORY = "./" # Temporary Download Directory
    BOT_NAME = "Seishiro Group Manger" # Bot Name
    WALL_API = "6950f53" # Wall API from wall.alphacoders.com
    ORIGINAL_EVENT_LOOP = True # Do not Change


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
