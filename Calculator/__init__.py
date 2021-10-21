from Core.Configurator import Configurator


calculator_config_path = './Calculator/config.ini'


def get_calculator_config(config_path):
    cr = Configurator()
    config = cr.load_config(config_path)

    return config


calculator_config = get_calculator_config(calculator_config_path)
