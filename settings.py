import os
from dotenv import load_dotenv

load_dotenv()

AUTH_TOKEN = os.getenv('AUTH_TOKEN')
API_URL = 'https://quack.duckduckgo.com/api/email/addresses'
DB_PATH = os.path.expanduser('~/.duck_emails.db')
