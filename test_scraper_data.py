from modules.scraper import NoonScraper

NOON_LINK = "https://www.noon.com/uae-ar/iphone-17-pro-max-256-gb-deep-blue-5g-esim-only-with-facetime-middle-east-version/N70211546V/p/?o=fd38748516cfc9fa&shareId=12a09b74-b376-4fd4-8a40-b2486d58d07b"

bot = NoonScraper()

try:
    result = bot.scrape_product(NOON_LINK)
    print("\n Final Scraped Return Verification:")
    print(f"-> Title box: {result['title']}")
    print(f"-> price box {result['price']}")

finally:
    bot.stop_browser()
