# Handles reading and providing the configuration to rest of program

import yaml

CONFIG_FILE = r"dtctl.yaml"
TOKEN = "token"
TENANT = "tenant"
API_VERSION = "defaultApiVersion"


class Config:

    def __init__(self):
        with open(CONFIG_FILE) as config_file:
            config = yaml.load(config_file, Loader=yaml.FullLoader)
            self.token = config[TOKEN]
            self.tenant = config[TENANT]
            self.auth_header = {'Authorization': 'Api-Token {token}'.format(token=self.token)}
            self.api_version = config[API_VERSION]
