import logging

class BotLogger:
    def __init__(self):

        self.logger = logging.getLogger("MyBot")
        self.logger.setLevel(logging.INFO)


        blueprint = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s', datefmt= '%H: %M: %S')
        if not self.logger.handlers:
            # Create a screen driver
            screen_driver = logging.StreamHandler()
            # Put our blueprint design onto the screen driver
            screen_driver.setFormatter(blueprint)
            # plug our driver onto our logging machine!
            self.logger.addHandler(screen_driver)



