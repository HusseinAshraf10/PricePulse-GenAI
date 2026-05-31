import os
import requests
from google import genai
from modules.logger import BotLogger


class PriceIntelligenceAnalyst:
    def __init__(self):
        self.log = BotLogger()
        self.client = genai.Client()
        self.telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")

    def generate_ai_report(self, raw_sheet_data):
        """Compiles spreadsheet matrix data and passes it to gemini-2.5-flash."""
        try:
            self.log.logger.info("Sending price history to Google Gemini...")

            data_summary = "\n".join([str(row) for row in raw_sheet_data[-10:]])

            prompt = (
                f"You are an expert E-Commerce Price Analyst tracking tech items in Egypt.\n"
                f"Analyze this raw historical pricing matrix (Format: [Date, Time, Title, Price]):\n\n"
                f"{data_summary}\n\n"
                f"Provide a concise, direct daily markdown report focusing on price trajectory updates, "
                f"trends, and a clear Buy or Wait action recommendation."
            )

            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )
            return response.text
        except Exception as error:
            self.log.logger.error(f"Gemini API processing failed: {error}")
            return "AI daily intelligence report generation failed due to system exception."

    def broadcast_to_telegram(self, report_text):
        """Sends the markdown text report straight to your Telegram device inbox."""
        try:
            self.log.logger.info("Transmitting report to Telegram API...")
            url = f"https://api.telegram.org/bot{self.telegram_token}/sendMessage"
            payload = {
                "chat_id": self.telegram_chat_id,
                "text": report_text,
                "parse_mode": "HTML"
            }
            response = requests.post(url, json= payload, timeout= 10)
            if response.status_code == 200:
                self.log.logger.info("Telegram AI reports broadcasted successfully!")
            else:
                self.log.logger.info(f"Telegram AI Error. Status code: {response.status_code}")
                self.log.logger.error(f"Server Response Context: {response.text}")
        except Exception as error:
            self.log.logger.error(f"Telegram network pipeline dropped: {error}")
