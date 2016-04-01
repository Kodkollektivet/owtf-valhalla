import json

def dump_config_json():
    """Read and return entire config file as json"""
    with open('config.json') as config_file:
        config = json.load(config_file)
    return config


def read_config(key):
    """Read and return the str value for a given key"""
    with open('config.json') as config_file:
        config = json.load(config_file)

    if key not in config:
        raise KeyError("The specified key '%s' does not exist" % key)
    else:
        return str(config[key])


def valid_cfg(config):
    """Simple key-check for a minimal configuration"""
    required_keys = {'title', 'description', 'command', 'arguments'}
    if not config.keys() >= required_keys:
        return False
    return True
            
