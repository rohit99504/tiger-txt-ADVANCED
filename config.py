import os

API_ID = os.environ.get("API_ID", "27498866") 

API_HASH = os.environ.get("API_HASH", "96fbb6ad2e11ab04e83ca09ef3f42455")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6996626836:AAE_7oV8JDqG2J-NcBGBbFSbnIjUz_okTHA")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", "6488911325"))

LOG_CH = -1002059340064

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6488911325").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


