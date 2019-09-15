import requests
import yaml
import dtctl_modules.shared_functions as shared

DASHBOARDS_ENDPOINT = '/api/config/v1/dashboards/'


class Dashboards:
    def __init__(self, config):
        self.config = config
        self.endpoint = self.config.tenant + DASHBOARDS_ENDPOINT
        self.type = "Dashboard"

    def list(self):
        return shared.list(self)

    def get_id(self, name):
        return shared.get_id_from_name(self, name)

    def get(self, dashboard_id):
        return shared.get(self, dashboard_id)

    def create(self, *config_files, directory=None):
        shared.create(self, *config_files, directory=directory)

    def update(self, dashboard_id, config_file):
        shared.update(self, dashboard_id, config_file)

    def delete(self, *dashboard_ids):
        shared.delete(self, *dashboard_ids)