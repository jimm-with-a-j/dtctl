# Class for the alerting profiles API endpoint

import requests
import yaml

ALERTING_PROFILES_ENDPOINT = '/api/config/v1/alertingProfiles/'


class AlertingProfiles:
    def __init__(self, config):
        self.config = config

    def list(self):
        response = requests.get(
            self.config.tenant + ALERTING_PROFILES_ENDPOINT,
            headers=self.config.auth_header
        )
        return response.json()['values']

    def get_id(self, name):
        alerting_profiles = self.list()
        matching_profiles = []
        for ap in alerting_profiles:
            if ap['name'] == name:
                matching_profiles.append(ap['id'])

        return matching_profiles

    def get(self, profile_id, output='JSON'):
        response = requests.get(
            self.config.tenant + ALERTING_PROFILES_ENDPOINT + profile_id,
            headers=self.config.auth_header
        ).json()

        if output == 'YAML':
            response = yaml.dump(response, default_flow_style=False)

        return response
