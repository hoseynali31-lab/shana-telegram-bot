import requests
import os

# ======================
# تنظیمات از GitHub Secrets یا محیط
# ======================
BOT_TOKEN = os.getenv("BOT_TOKEN")       # توکن ربات
CHAT_ID = os.getenv("CHAT_ID")           # chat_id گروه

# ======================
# پیام تست
# ======================
msg = "✅ این یک تست ربات تلگرام است. همه چیز درست کار می‌کند."

# ======================
# ارسال به تلگرام
# ======================
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
response = requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

if response.status_code == 200:
    print("پیام تست با موفقیت ارسال شد!")
else:
    print("ارسال پیام موفق نبود:", response.text)
