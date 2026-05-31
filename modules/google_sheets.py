import sys
import urllib3

# Set up the memory redirect safety nets FIRST
sys.modules['requests.packages.urllib3'] = urllib3
sys.modules['requests.packages.urllib3.util.ssl_'] = urllib3.util.ssl_
import gspread
from modules.logger import BotLogger


class GoogleSheetsClient:
    def __init__(self):
        self.log_notebook = BotLogger()
        self.sheet_name = "Price_Intelligence_Data"

        self.client = None
        self.config_sheet = None
        self.log_sheet = None

        self.connect_to_google()

    def connect_to_google(self):
        """presents our JSON badge to log into Google sheets."""
        try:
            self.log_notebook.logger.info("presenting security badge to Google Cloud...")
            # Use gspread to log in using our credential file
            self.client = gspread.service_account(filename="service_account.json")
            self.log_notebook.logger.info(f"Opening spreadsheet: '{self.sheet_name}'...")

            workbook = self.client.open(self.sheet_name)

            # Upgraded Layer: Target both individual tabs explicitly
            self.config_sheet = workbook.worksheet("Products_Config")
            self.log_sheet = workbook.worksheet("Price_Log")

            self.log_notebook.logger.info("Google Sheets connection established perfectly!")

        except Exception as error:
            self.log_notebook.logger.error(f"Failed to connect to Google Sheets: {error}")

    def get_tracked_products(self):
        """Extracts all product names and URLs from the Products_Config tab."""
        try:
            # Reads row 1 as keys, returns a list of dictionary pairs
            return self.config_sheet.get_all_records()
        except Exception as error:
            self.log_notebook.logger.error(f"Failed to read configuration rows: {error}")
            return []


    def append_price_row(self, date_str, time_str, title_str, price_str):
        """Inserts a brand-new row of live tracking data into the spreadsheet."""

        try:
            self.log_notebook.logger.info(f"Preparing to write data row for: {price_str} EGP...")

            new_row_data = [date_str, time_str, title_str, price_str]
            self.log_sheet.append_row(new_row_data)
            self.log_notebook.logger.info("Row successfully saved into Price log tab!")
        except Exception as error:
            self.log_notebook.logger.error(f"Failed to write row data: {error}")


    def get_price_history_matrix(self):
        """Downloads the full raw text history table from the Price_Log tab for Gemini."""
        try:
            return self.log_sheet.get_all_values()
        except Exception as error:
            self.log_notebook.logger.error(f"Failed to read price history matrix: {error}")
            return []