# Class for the alerting management zones API endpoint

import requests
import yaml
import dtctl_modules.shared_functions as shared

MANAGEMENT_ZONES_ENDPOINT = '/api/config/v1/managementZones/'


class ManagementZones:
    def __init__(self, config):
        self.config = config

    def list(self):
        success, zone_list_json = shared.get_json(self.config.tenant + MANAGEMENT_ZONES_ENDPOINT,
                                           self.config.auth_header)
        if success:
            zone_list_json = zone_list_json['values']

        return zone_list_json

    def get_id(self, name):
        return shared.get_id_from_name(name, self.list())

    def get(self, zone_id):
        response = requests.get(self.config.tenant + MANAGEMENT_ZONES_ENDPOINT + str(zone_id),
                                headers=self.config.auth_header
                                )
        return yaml.safe_dump(response.json(), default_flow_style=False)

    def create(self, *config_files, directory=None):
        for config_file in config_files:
            created = shared.validate_and_send(self, config_file,
                                               self.config.tenant + MANAGEMENT_ZONES_ENDPOINT,
                                               self.config.auth_header,
                                               "create")
        return

    def delete(self, *zone_ids):
        pass

    def exists(self, zone_id):
        return shared.exists(self, zone_id)

