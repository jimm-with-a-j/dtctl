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
        success, profile_list_json = shared.get_json(self)
        if success:
            profile_list_json = profile_list_json['values']
        return profile_list_json

    def get_id(self, name):
        return shared.get_id_from_name(self, name)

    def get(self, profile_id):
        return shared.get(self, profile_id)

    def create(self, *config_files):
        for config_file in config_files:
            created = shared.validate_and_send(self, config_file)

    def update(self, profile_id, config_file):
        shared.update(self, profile_id, config_file)

    def delete(self, *profile_ids):
        for profile_id in profile_ids:
            try:
                assert (shared.exists(profile_id))
                deletion_response = requests.delete(
                    self.config.tenant + ALERTING_PROFILES_ENDPOINT + profile_id,
                    headers=self.config.auth_header
                ).status_code
                if deletion_response == SUCCESS_UNMODIFIED:
                    print("Profile {id} deleted successfully (response: {code})"
                          .format(id=profile_id, code=deletion_response))
                else:
                    print("Error returned when deleting profile " + profile_id)
            except AssertionError as assert_exception:
                print("The specified profile id {id} does not exist in the environment".format(id=profile_id))

        return
