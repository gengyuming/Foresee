from Core.configurator import Configurator


core_config_path = './Core/config.ini'


def get_core_config(config_path):
    cr = Configurator()
    config = cr.load_config(config_path)

    return config


core_config = get_core_config(core_config_path)
