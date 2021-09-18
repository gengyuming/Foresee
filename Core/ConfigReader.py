# -*- encoding: utf-8 -*-
import configparser


class ConfigReader:
    @staticmethod
    def load_config(config_path):
        config_file = configparser.RawConfigParser()
        config_file.read(config_path, 'utf-8')

        return config_file
