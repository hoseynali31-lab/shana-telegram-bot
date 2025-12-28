from playwright.sync_api import sync_playwright
import requests
import jdatetime
import os

# ======================
# تنظیمات
# ======================
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

KEYWORDS = [
    "مکانیکال کانکتور",
    "کلمپ",
    "clamp",
    "connector"
]

URL = "https://www.shana.ir/page/shana/module/tenderSearch.xhtml"

# ======================
# تاریخ امروز به فرمت سایت
# ======================
today_j = jdatetime.date.today()
MONTHS = ["فروردین","اردیبهشت","خرداد","تیر","مرداد","شهریور",
          "مهر","آبان","آذر","دی","بهمن","اسفند"]
today_text = f"{today_j.day} {MONTHS[today_j.month-1]} {today_j.year}"

# ======================
# تابع ارسال به تلگرام
# ======================
def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg[:4000]})

# ======================
# Scraper
# ======================
titles = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(URL, timeout=60000)

    # پیدا کردن تعداد کل صفحات
    pages = page.query_selector_all("div.ui-paginator-pages span")
    total_pages = int(pages[-1].inner_text()) if pages else 1

    # بررسی 5 صفحه آخر
    start_page = max(total_pages - 4, 1)

    for p_num in range(start_page, total_pages + 1):
        if p_num > 1:
            page.click(f"text='{p_num}'")
            page.wait_for_timeout(3000)  # صبر برای بارگذاری صفحه

        rows = page.query_selector_all("table tbody tr")
        for row in rows:
            cells = row.query_selector_all("td")
            if len(cells) < 2:
                continue

            title_text = cells[1].inner_text().strip()  # ستون عنوان
            if any(k.lower() in title_text.lower() for k in KEYWORDS):
                titles.append(title_text)

    browser.close()

# ======================
# ارسال پیام
# ======================
if titles:
    msg = "📌 آگهی‌های مرتبط (۵ صفحه آخر):\n\n"
    for i, t in enumerate(titles, 1):
        msg += f"{i}. {t}\n"
else:
    msg = "❌ آگهی مرتبطی پیدا نشد."

send_telegram(msg)
