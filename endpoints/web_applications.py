import requests
import yaml
import dtctl_modules.shared_functions as shared

WEB_APPLICATIONS_ENDPOINT = '/api/config/v1/applications/web/'


class WebApplications:
    def __init__(self, config):
        self.config = config
        self.endpoint = self.config.tenant + WEB_APPLICATIONS_ENDPOINT
        self.type = "Web application"

    def list(self):
        return shared.list(self)

    def get_id(self, name):
        return shared.get_id_from_name(self, name)

    def get(self, web_application_id, config_type=None):
        if config_type == "privacy":
            return shared.get(self, web_application_id, path_modifier="/dataPrivacy")
        else:
            return shared.get(self, web_application_id)

    def get_privacy(self, web_application_id):
        return shared.get(self, web_application_id, path_modifier="/dataPrivacy")

    def create(self, *config_files, directory=None):
        shared.create(self, *config_files, directory=directory)

    def update(self, web_application_id, config_file):
        shared.update(self, web_application_id, config_file)

    def update_privacy(self, web_application_id, config_file):
        shared.update(self, web_application_id, config_file, path_modifier='/dataPrivacy')

    def delete(self, *web_application_ids):
        shared.delete(self, *web_application_ids)