# Class for the alerting profiles API endpoint

import requests
import yaml
from dtctl_modules.shared_functions import validate_and_send

ALERTING_PROFILES_ENDPOINT = '/api/config/v1/alertingProfiles/'
SUCCESS_UNMODIFIED = 204


class AlertingProfiles:
    def __init__(self, config):
        self.config = config

    def list(self):
        """Returns basic info on alerting profiles"""

        response = requests.get(
            self.config.tenant + ALERTING_PROFILES_ENDPOINT,
            headers=self.config.auth_header
        )

        return response.json()['values']

    def get_id(self, name):
        """Returns a list of ids for all profiles that match provided name"""

        alerting_profiles = self.list()  # uses list function to get all alerting profiles
        matching_profiles = []

        for ap in alerting_profiles:
            if ap['name'] == name:
                matching_profiles.append(ap['id'])

        return matching_profiles

    def get(self, profile_id, output='JSON'):
        """
        Returns the configuration for specified alerting profile (by id)

        Specify --output=YAML to get output in yaml format
        """

        response = requests.get(
            self.config.tenant + ALERTING_PROFILES_ENDPOINT + str(profile_id),
            headers=self.config.auth_header
        ).json()

        if output == 'YAML':
            response = yaml.safe_dump(response, default_flow_style=False)

        return response

    def create(self, *config_files):
        """
        Creates an alerting profile using a provide file

        :param config_file:
        :return:
        """

        for config_file in config_files:
            created = validate_and_send(
                    config_file,
                    self.config.tenant + ALERTING_PROFILES_ENDPOINT,
                    self.config.auth_header,
                    "create"
                    )

        return

    def update(self, profile_id, config_file):
        """
        Creates an alerting profile using a provide file

        :param profile_id:
        :param config_file:
        :return:
        """

        try:
            assert (self.exists(profile_id))
            updated = validate_and_send(
                    config_file,
                    self.config.tenant + ALERTING_PROFILES_ENDPOINT + str(profile_id) + '/',
                    self.config.auth_header,
                    "update"
                    )
        except AssertionError as assert_exception:
            print("The specified profile id {id} does not exist in the environment".format(id=profile_id))

        return

    def delete(self, *profile_ids):
        """
        Removes the specified alerting profiles

        :param profile_ids:
        :return:
        """
        for profile_id in profile_ids:
            try:
                assert (self.exists(profile_id))
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

    def exists(self, profile_id):
        """
        Checks that the profile with specified id exists

        :param profile_id:
        :return:
        """
        alerting_profiles = self.list()
        ap_exists = False
        for ap in alerting_profiles:
            if ap['id'] == profile_id:
                ap_exists = True

        return ap_exists
