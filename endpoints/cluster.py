# Thinking this will be a class for general cluster information

import requests

VERSION_ENDPOINT = '/api/v1/config/clusterversion'
TIME_ENDPOINT = '/api/v1/time'


class Cluster:
    def __init__(self, config):
        self.config = config

    def version(self):
        response = requests.get(
            self.config.tenant + VERSION_ENDPOINT,
            headers=self.config.auth_header
        )
        return response.json()['version']

    def time(self):
        response = requests.get(
            self.config.tenant + TIME_ENDPOINT,
            headers=self.config.auth_header
        )
        return response.json()
