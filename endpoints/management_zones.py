# Class for the alerting management zones API endpoint

import requests
import yaml
import dtctl_modules.shared_functions as shared

MANAGEMENT_ZONES_ENDPOINT = '/api/config/v1/managementZones/'


class ManagementZones:
    def __init__(self, config):
        self.config = config
        self.endpoint = self.config.tenant + MANAGEMENT_ZONES_ENDPOINT
        self.type = "Management zone"

    def list(self):
        return shared.list(self)

    def get_id(self, name):
        return shared.get_id_from_name(self, name)

    def get(self, zone_id):
        return shared.get(self, zone_id)

    def create(self, *config_files, directory=None):
        shared.create(self, *config_files, directory=directory)

    def update(self, zone_id, config_file):
        shared.update(self, zone_id, config_file)

    def delete(self, *zone_ids):
        shared.delete(self, *zone_ids)

