from modules.scraper import NoonScraper

scraper_bot = NoonScraper()

try:
    scraper_bot.start_browser()
    print("\n--- Both Logger and Scraper OOP skeletons are talking perfectly! ---\n")

finally:
    scraper_bot.stop_browser()
