# 🤖 AI-Driven Multi-Product Price Intelligence Bot

A production-ready E-Commerce tracking pipeline that automatically scans product grids, maintains a cloud database matrix, and uses Google Gemini to stream daily market analytics reports directly to a user's phone via Telegram.

---

## ⚙️ Features
* **Automated Data Scraping:** Reuses a single headless browser core to sequentially target product parameters.
* **Google Sheets Matrix Integration:** Dynamically interfaces with multiple tab worksheets for configurations and logging.
* **Gemini 2.5 Intelligence Engine:** Passes localized historical pricing tables directly to AI to evaluate market trajectory adjustments.
* **24/7 Serverless Execution:** Programmed to trigger automatically completely free via GitHub Actions virtual machines.

---

## 🛠️ Setup Instructions for Developers

### 1. Database Setup
1. Create a copy of a Google Spreadsheet workbook named `Price_Intelligence_Data`.
2. Add two distinct worksheet tabs:
   * **`Products_Config`**: Column A: `Product Name` | Column B: `Noon URL`
   * **`Price_Log`**: Column A: `Date` | Column B: `Time` | Column C: `Product Title` | Column D: `Price`
3. Generate a Google Cloud Service Account JSON key credential file and give it access to your spreadsheet workbook.

### 2. GitHub Secrets Configuration
Fork or duplicate this repository, navigate to your repository **Settings -> Secrets and Variables -> Actions**, and add these precise encrypted keys:

| Secret Key | Description |
|---|---|
| `GEMINI_API_KEY` | Your Google AI developer key credentials. |
| `TELEGRAM_BOT_TOKEN` | HTTP API access identifier string token created via BotFather. |
| `TELEGRAM_CHAT_ID` | Your unique Telegram numeric identity destination window channel coordinate. |
| `GOOGLE_SERVICE_ACCOUNT_JSON` | The absolute raw text content copy-pasted straight out of your private `service_account.json` file. |

---

## 🏃‍♂️ Running the Engine
* **Cloud Automation:** The system executes automatically every single day at **09:00 AM (Egypt Time / UTC+2)** using the cron scheduler loop mapping embedded inside `.github/workflows/run_bot.yml`.
* **Manual Override:** Go to your GitHub repository -> click **Actions** tab -> select **Daily Price Intelligence Automation** -> click **Run workflow** to force execution instantly.