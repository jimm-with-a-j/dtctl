# Class for the alerting auto tags endpoint

import requests
import yaml
import dtctl_modules.shared_functions as shared

AUTO_TAGS_ENDPOINT = '/api/config/v1/autoTags/'


class AutoTags:
    def __init__(self, config):
        self.config = config
        self.endpoint = self.config.tenant + AUTO_TAGS_ENDPOINT
        self.type = "Auto tag rule"

    def list(self):
        return shared.list(self)

    def get_id(self, name):
        return shared.get_id_from_name(self, name)

    def get(self, zone_id):
        return shared.get(self, zone_id)

    def create(self, *config_files, directory=None):
        shared.create(self, *config_files, directory=directory)

    def update(self, tag_id, config_file):
        shared.update(self, tag_id, config_file)

    def delete(self, *zone_ids):
        shared.delete(self, *zone_ids)
