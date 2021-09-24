# -*- encoding: utf-8 -*-
import configparser


core_config_path = './Core/config.ini'


class ConfigReader:
    @staticmethod
    def load_config(config_path):
        config_file = configparser.RawConfigParser()
        config_file.read(config_path, 'utf-8')

        return config_file


class CoreConfig:

    @staticmethod
    def get_core_config():
        cr = ConfigReader()
        config = cr.load_config(core_config_path)

        return config


core_config = CoreConfig().get_core_config()



