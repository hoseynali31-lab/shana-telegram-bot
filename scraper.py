import requests
import os

BOT_TOKEN = 8371006264:AAHKeeQ5VochtU7pAQeqqGY4z_xALRHO9tM
CHAT_ID = -1003562926125

msg = "✅ تست ربات: همه چیز درست کار می‌کند."

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
response = requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

print(response.status_code, response.text)
