import configparser

config = configparser.RawConfigParser()
config.read("/Users/sayantabera/My_Work_Folder/Python_Projects/nopCommerceApp/Configuration/config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
