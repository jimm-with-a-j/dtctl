# common functions for sending and validating configs

import requests
import yaml

VALID = 204
SUCCESS = 201


def validate_and_send(config_file, target, headers, method):
    """
    Validates and posts a YAML config file to the specified endpoint


    """

    success = False
    try:
        with open(config_file, "r") as file:
            try:
                json_payload = yaml.safe_load(file)
                validation_response = requests.post(target + 'validator', headers=headers, json=json_payload)
                if validation_response.status_code == VALID:

                    # An update vs creation is just a put vs a post http method
                    if method == "create":
                        creation_response = requests.post(target, headers=headers, json=json_payload)
                    if method == "update":
                        creation_response = requests.put(target, headers=headers, json=json_payload)
                    print(creation_response.status_code)
                    if creation_response.status_code == SUCCESS:
                        success = True
                    else:
                        success = False
            except yaml.YAMLError as exc:
                print("Some issue loading your yaml, please verify it is valid.")
                print(exc)
    except FileNotFoundError as exc:
        print("File {file} could not be found".format(file=config_file))
    return success
