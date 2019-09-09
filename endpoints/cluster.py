# Thinking this will be a class for general cluster information

import requests


class Cluster:
    def __init__(self, config):
        self.config = config

    def version(self):
        response = requests.get(
            self.config.tenant + '/api/v1/config/clusterversion',
            headers=self.config.auth_header
        )
        return response.json()['version']

    def time(self):
        response = requests.get(
            self.config.tenant + '/api/v1/time',
            headers=self.config.auth_header
        )
        return response.json()