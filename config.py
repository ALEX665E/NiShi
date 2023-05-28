from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/fd2d1b9bdef248cd900f9.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/e6bd1a3f1fe9a62328b07.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/indian_chatting_club_offical")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/tha_govind_op")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1864894033").split()))


FAILED = "https://telegra.ph/file/db8765da6945e3c9333e6.jpg"
