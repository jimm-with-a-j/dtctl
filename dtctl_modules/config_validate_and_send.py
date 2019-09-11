# common functions for sending and validating configs

import requests
import yaml

VALIDATION_OK = 204


def validate_and_send(config_file, target, headers, validationTarget=None):
    """
    Validates and posts a YAML config file to the specified endpoint


    :param config_file:
    :param target:
    :param headers:
    :param validationTarget:
    :return:
    """

    with open(config_file, "r") as file:
        try:
            json_payload = yaml.safe_load(file)
            validation_response = requests.post(target + 'validator', headers=headers, json=json_payload)
            if validation_response.status_code == VALIDATION_OK:
                creation_response = requests.post(target, headers=headers, json=json_payload)
        except yaml.YAMLError as exc:
            print("Some issue loading your yaml, please verify it is valid.")
            print(exc)

    return creation_response.json()
