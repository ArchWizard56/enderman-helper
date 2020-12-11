import configparser

CONFIG = configparser.ConfigParser()

CONFIG.read("config.ini")

class BOT:
    token = CONFIG["BOT"]["token"]
    prefix = CONFIG["BOT"]["prefix"]
    status = CONFIG["BOT"]["status"]

class SERVER:
    host = CONFIG["SERVER"]["host"]
    port = CONFIG["SERVER"]["port"]
    id = CONFIG["SERVER"]["id"]

class DISCORD:
    chatChannel = CONFIG["DISCORD"]["chatChannel"]
    consoleChannel = CONFIG["DISCORD"]["consoleChannel"]

class API:
    apiUrl = CONFIG["API"]["apiUrl"]
    apiKey = CONFIG["API"]["apiKey"]

bot = BOT()
discord = DISCORD()
server = SERVER()
api = API()