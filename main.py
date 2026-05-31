import os
import time
from dotenv import load_dotenv
from datetime import datetime,  timedelta
from modules.logger import BotLogger
from modules.scraper import NoonScraper
from modules.google_sheets import GoogleSheetsClient
from modules.intelligence import PriceIntelligenceAnalyst


load_dotenv()
def run_price_tracker():
    log = BotLogger()
    log.logger.info("Starting the Price Intelligence Pipeline automation...")

    product_URL = os.getenv("TARGET_PRODUCT_URL")
    scraper = NoonScraper()
    sheets_client = GoogleSheetsClient()
    analyst = PriceIntelligenceAnalyst()

    try:
        products_to_track = sheets_client.get_tracked_products()
        if not products_to_track:
            log.logger.error("The Products_Config matrix returned empty. Halting pipeline run.")
            return

        log.logger.info(f"Detected {len(products_to_track)} target products inside your configuration.")

        for index, product in enumerate(products_to_track, start=1):
            name = product.get("Product Name")
            url = product.get("Noon URL")

            log.logger.info(f"[{index}/{len(products_to_track)}] Processing target tracker: {name}")

            if not url:
                log.logger.warning(f"Empty link field skipped for row entry: {name}")
                continue

            scraped_item = scraper.scrape_product(url)
            if scraped_item["title"] != "Error":
                now = datetime.now()
                current_date, current_time = now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S")

                sheets_client.append_price_row(
                    current_date,
                    current_time,
                    scraped_item["title"],
                    scraped_item["price"],
                )
            else:
                log.logger.error("Scraper encountered an error page. Skipping Google Sheets write step.")

        # Generate Gemini analysis and broadcast to phone
        historical_matrix = sheets_client.get_price_history_matrix()
        ai_report = analyst.generate_ai_report(historical_matrix)
        analyst.broadcast_to_telegram(ai_report)


    finally:
        log.logger.info("Cleaning up background browser runtime instances...")
        scraper.stop_browser()
        log.logger.info("Multi-Product Pipeline run sequence complete.")

if __name__ == "__main__":
    log = BotLogger()
    log.logger.info("Price Intelligence System scheduling engine initialized.")
    run_price_tracker()
    # while True:
    #     try:
    #         now = datetime.now()
    #         target_time = now.replace(hour=9, minute=0, second=0, microsecond=0)
    #
    #         # If it's already past 9:00 AM, calculate the wait time for 9:00 AM TOMORROW
    #         if now >= target_time:
    #             from datetime import timedelta
    #             target_time += timedelta(days=1)
    #
    #
    #         seconds_to_wait = (target_time - now).total_seconds()
    #         log.logger.info(
    #             f"System resting. Next pipeline run scheduled for {target_time} (Waiting {seconds_to_wait:.0f} seconds)...")
    #
    #         time.sleep(seconds_to_wait)
    #         run_price_tracker()
    #
    #     except KeyboardInterrupt:
    #         log.logger.info("Automation loop terminated safely by user request.")
    #         break
    #     except Exception as system_error:
    #         log.logger.error(f"Critical scheduler exception encountered: {system_error}")
    #         time.sleep(60)