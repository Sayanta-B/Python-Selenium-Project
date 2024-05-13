import logging

class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename="/Users/sayantabera/My_Work_Folder/Python_Projects/nopCommerceApp/Logs/automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

