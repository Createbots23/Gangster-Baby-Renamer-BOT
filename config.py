import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21740783")

API_HASH = os.environ.get("API_HASH", "a5dc7fec8302615f5b441ec5e238cd46")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1002005436412") 

DB_NAME = os.environ.get("DB_NAME","Speedwolf1")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Speedwolf1:speedwolf24689@cluster0.rgfywsf.mongodb.net/")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/14cd2977df4d3ede888e0.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6299192020').split()]

PORT = os.environ.get("PORT", "8080")
