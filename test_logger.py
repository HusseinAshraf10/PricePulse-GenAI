from modules.logger import BotLogger

bot_notebook = BotLogger()

bot_notebook.logger.info("the bot has woken up")

bot_notebook.logger.warning("the website is taking a long time to load")

bot_notebook.logger.error("oh no, the phone price button disappeared")
