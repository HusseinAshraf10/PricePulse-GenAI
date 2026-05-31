from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from modules.logger import BotLogger

class NoonScraper:
    """Manages the background Chrome browser and bypasses anti-bot blocks."""

    def __init__(self):
        self.log_notebook = BotLogger()
        self.chrome_options = Options()
        self._configure_browser_settings()
        self.driver = None

    # prepares the secret passport flags to look like a human browser
    def _configure_browser_settings(self):
        self.chrome_options.add_argument("--headless=new")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-div-shm-usge")

        human_password = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        self.chrome_options.add_argument(f"user-agent={human_password}")

    def start_browser(self):
        """Safely turns on the browser engine"""

        try:
            self.log_notebook.logger.info("Turing on the background Chrome engine")
            self.driver = webdriver.Chrome(options= self.chrome_options)
            self.driver.maximize_window()
            self.log_notebook.logger.info("Browser is running smoothly in the background")
        except WebDriverException as error:
            self.log_notebook.logger.error(f"Filed to start Chrome: {error}")
            raise

    def scrape_product(self, product_url):
        """Navigates to Noon item url and extracts its Title and Price."""
        # 1. If the browser isn't turned on yet, turn it on!
        if not self.driver:
            self.start_browser()

        try:
            self.log_notebook.logger.info(f"Driving browser to products page")
            self.driver.get(product_url)

            # 2. Setup our smart lookout helper (Wait up to 15 seconds max) and expected_conditions and By
            from selenium.webdriver.support.wait import WebDriverWait
            from selenium.webdriver.support import expected_conditions as ec
            from selenium.webdriver.common.by import By

            lookout = WebDriverWait(self.driver, 15)

            # 3. Tell the lookout to wait until the h1 title is fully loaded on screen
            self.log_notebook.logger.info("Scanning page layout for products element")
            title_element = (lookout.until
                             (ec.presence_of_element_located
                              ((By.CSS_SELECTOR, ".ProductTitle-module-scss-module__EXiEUa__title"))))

            # 4. Tell the lookout to wait until the price element is fully loaded
            price_element = (lookout.until
                             (ec.presence_of_element_located
                              ((By.CLASS_NAME, 'PriceOfferV2-module-scss-module__dHtRPW__priceNowText'))))
            # 5. Pack the clean text data into a neat Python dictionary box
            scraped_data = {
                "title": title_element.text.strip(),
                "price": price_element.text,
            }

            self.log_notebook.logger.info(f"Success found: {scraped_data['title'][:30]} price {scraped_data['price']}")
            return scraped_data
        # 6. except part
        except Exception as error:
            self.log_notebook.logger.info(f"Filed to extract product data: {error}")
            return {"title": "Error", "price": "0"}

    def stop_browser(self):
        """Safely shut down the browser to save your computer's memory"""

        if self.driver:
            self.driver.quit()
            self.log_notebook.logger.info("Browser engine shut down safely")