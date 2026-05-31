from datetime import datetime
from modules.google_sheets import GoogleSheetsClient

sheets_bot = GoogleSheetsClient()
now = datetime.now()
current_date, current_time = now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S")

try:
    sheets_bot.append_price_row(current_date, current_time, "Test iPhone 17", "5399.00")

finally:
    print("All done successfully!")
