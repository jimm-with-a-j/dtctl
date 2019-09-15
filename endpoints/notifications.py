import requests
import yaml
import dtctl_modules.shared_functions as shared

NOTIFICATIONS_ENDPOINT = '/api/config/v1/notifications/'


class Notifications:
    def __init__(self, config):
        self.config = config
        self.endpoint = self.config.tenant + NOTIFICATIONS_ENDPOINT
        self.type = "Notification"

    def list(self):
        return shared.list(self)

    def get_id(self, name):
        return shared.get_id_from_name(self, name)

    def get(self, notification_id):
        return shared.get(self, notification_id)

    def create(self, *config_files, directory=None):
        shared.create(self, *config_files, directory=directory)

    def update(self, notification_id, config_file):
        shared.update(self, notification_id, config_file)

    def delete(self, *notification_ids):
        shared.delete(self, *notification_ids)