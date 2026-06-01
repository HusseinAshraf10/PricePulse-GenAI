 PricePulse-GenAI
 
An automated price monitoring bot that tracks Noon.com products daily, analyzes price trends with Gemini 2.5, and sends a morning report straight to your phone via Telegram.
Built with Python, Selenium, Google Sheets, and GitHub Actions — runs completely free, every day, with zero manual work.

How It Works

Scrapes product prices from Noon.com using headless Selenium
Logs everything to Google Sheets across two tabs — product config and price history
Analyzes the price history with Gemini 2.5 Flash to detect trends and highlight deals
Delivers a daily intelligence report to your Telegram every morning at 9am
Runs automatically via GitHub Actions — no server, no cost, no maintenance


Setup
1. Google Sheets
Create a spreadsheet named Price_Intelligence_Data with two tabs:

Products_Config — Column A: Product Name | Column B: Noon URL
Price_Log — Date | Time | Product Title | Price

Generate a Google Cloud Service Account, download the JSON key, and share your spreadsheet with the service account email.
2. GitHub Secrets
Fork this repo, go to Settings → Secrets → Actions, and add:
SecretWhat it isGEMINI_API_KEYYour Google AI API keyTELEGRAM_BOT_TOKENToken from BotFather on TelegramTELEGRAM_CHAT_IDYour Telegram chat IDGOOGLE_SERVICE_ACCOUNT_JSONFull contents of your service_account.json file

Running It
Automatic: Runs every day at 9:00 AM Egypt time via the GitHub Actions workflow.
Manual: Go to Actions → Daily Price Intelligence Automation → Run workflow.

Developed by @HusseinAshraf10

## Running the Engine
* **Cloud Automation:** The system executes automatically every single day at **09:00 AM (Egypt Time / UTC+2)** using the cron scheduler loop mapping embedded inside `.github/workflows/run_bot.yml`.
* **Manual Override:** Go to your GitHub repository -> click **Actions** tab -> select **Daily Price Intelligence Automation** -> click **Run workflow** to force execution instantly.
