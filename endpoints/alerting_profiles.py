# Class for the alerting profiles API endpoint

import requests
import yaml
import dtctl_modules.shared_functions as shared

ALERTING_PROFILES_ENDPOINT = '/api/config/v1/alertingProfiles/'
SUCCESS_UNMODIFIED = 204


class AlertingProfiles:
    def __init__(self, config):
        self.config = config
        self.endpoint = self.config.tenant + ALERTING_PROFILES_ENDPOINT

    def list(self):
        return shared.list(self)

    def get_id(self, name):
        return shared.get_id_from_name(self, name)

    def get(self, profile_id):
        return shared.get(self, profile_id)

    def create(self, *config_files):
        shared.create(self, *config_files)

    def update(self, profile_id, config_file):
        shared.update(self, profile_id, config_file)

    def delete(self, *profile_ids):
        shared.delete(self, *profile_ids)
