# Class for the alerting management zones API endpoint

import requests
import yaml
from dtctl_modules.shared_functions import validate_and_send, get_json, get_id_from_name

MANAGEMENT_ZONES_ENDPOINT = '/api/config/v1/managementZones/'
SUCCESS_UNMODIFIED = 204


class ManagementZones:
    def __init__(self, config):
        self.config = config

    def list(self):
        success, zone_list_json = get_json(self.config.tenant + MANAGEMENT_ZONES_ENDPOINT,
                                           self.config.auth_header)
        if success:
            zone_list_json = zone_list_json['values']

        return zone_list_json

    def get_id(self, name):
        return get_id_from_name(name, self.list())


