import configparser

config = configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")


class ReadConfig:

    def get_base_url(self):
        base_url = config.get("common info", "base_url")
        return base_url

    def get_username(self):
        base_url = config.get("common info", "username")
        return base_url

    def get_password(self):
        base_url = config.get("common info", "password")
        return base_url
