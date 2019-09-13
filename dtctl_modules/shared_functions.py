# common functions for sending and validating configs

import requests
import yaml

SUCCESS_UNMODIFIED = 204
SUCCESS = 201


def validate_and_send(config_file, target, headers, method):
    """
    Validates and posts a YAML config file to the specified endpoint

    :param config_file:
    :param target:
    :param headers:
    :param method:
    :return:
    """
    success = False  # whether or not the change was successfully applied

    try:
        with open(config_file, "r") as file:
            try:
                json_payload = yaml.safe_load(file)
                validation_response = requests.post(target + 'validator', headers=headers, json=json_payload)
                if validation_response.status_code == SUCCESS_UNMODIFIED:
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
                else:
                    print(validation_response.json())
            except yaml.YAMLError as exc:
                print("Some issue loading your yaml, please verify it is valid.")
                print(exc)
            except Exception as e:
                print(e)

    except FileNotFoundError as exc:
        print("File {file} could not be found".format(file=config_file))
    except Exception as e:
        print(e)

    return success


def get_json(target, headers):
    success = False
    response = requests.get(target, headers=headers)
    response_json = response.json()
    if str(response.status_code).startswith('2'):
        success = True
    else:
        print("Error calling {target}, response code: {code}".format(target=target, code=response.status_code))

    return success, response_json


def get_id_from_name(name, item_list):
    match_list = []
    for item in item_list:
        if item['name'] == name:
            match_list.append(item['id'])
    if match_list == []:
        print("No matches for name {name}".format(name=name))
    return match_list
