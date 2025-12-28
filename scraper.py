import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

msg = "✅ تست ربات: همه چیز درست کار می‌کند."

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
response = requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

print(response.status_code, response.text)
