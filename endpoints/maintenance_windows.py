# Class for the alerting management zones API endpoint

import requests
import yaml
import dtctl_modules.shared_functions as shared

MAINTENANCE_WINDOWS_ENDPOINT = '/api/config/v1/maintenanceWindows/'


class MaintenanceWindows:
    def __init__(self, config):
        self.config = config
        self.endpoint = self.config.tenant + MAINTENANCE_WINDOWS_ENDPOINT

    def list(self):
        return shared.list(self)

    def get_id(self, name):
        return shared.get_id_from_name(self, name)

    def get(self, window_id):
        return shared.get(self, window_id)

    def create(self, *config_files, directory=None):
        shared.create(self, *config_files)

    def update(self, window_id, config_file):
        shared.update(self, window_id, config_file)

    def delete(self, *window_ids):
        shared.delete(self, *window_ids)