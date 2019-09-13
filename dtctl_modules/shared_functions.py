# common functions for sending and validating configs

import requests
import yaml


def validate_and_send(self, config_file, config_id=None):

    success = False  # whether or not the change was successfully applied

    try:
        with open(config_file, "r") as file:
            try:
                json_payload = yaml.safe_load(file)
                validation_response = requests.post(self.endpoint + 'validator', headers=self.config.auth_header, json=json_payload)
                if str(validation_response.status_code).startswith('2'):
                    # An update vs creation is just a put vs a post http method
                    if config_id is None:
                        response = requests.post(self.endpoint, headers=self.config.auth_header, json=json_payload)
                    if config_id is not None:
                        response = requests.put(self.endpoint + config_id, headers=self.config.auth_header, json=json_payload)
                    print(response.status_code)
                    if str(response.status_code).startswith('2'):
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


def get_json(self):
    success = False
    response = requests.get(self.endpoint, headers=self.config.auth_header)
    response_json = response.json()
    if str(response.status_code).startswith('2'):
        success = True
    else:
        print("Error calling {target}, response code: {code}".format(target=target, code=response.status_code))

    return success, response_json


def get_id_from_name(self, name):
    match_list = []
    for item in self.list():
        if item['name'] == name:
            match_list.append(item['id'])
    if match_list == []:
        print("No matches for name {name}".format(name=name))
    return match_list


def exists(self, config_id):
    config_id = str(config_id)
    config_list = self.list()
    config_exists = False
    for config in config_list:
        if config['id'] == config_id:
            config_exists = True
    return config_exists


def get(self, config_id):
    response = requests.get(self.endpoint + str(config_id), headers=self.config.auth_header)
    return yaml.safe_dump(response.json(), default_flow_style=False)


def update(self, config_id, config_file):
    config_id = str(config_id)
    try:
        assert (exists(self, config_id))
        updated = validate_and_send(self, config_file, config_id)
    except AssertionError as e:
        print("{id} does not exist in the environment".format(id=config_id))


def delete(self, *config_ids):
    for config_id in config_ids:
        try:
            assert (exists(self, config_id))
            deletion_response = requests.delete(self.endpoint + config_id, headers=self.config.auth_header).status_code
            if str(deletion_response).startswith('2'):
                print("Config {id} deleted successfully (response: {code})"
                      .format(id=config_id, code=deletion_response))
            else:
                print("Error returned when deleting profile " + config_id)
        except AssertionError as e:
            print("Config {id} does not exist in the environment".format(id=config_id))


def list(self):
    success, config_list_json = get_json(self)
    if success:
        config_list_json = config_list_json['values']
    return config_list_json


def create(self, *config_files):
    for config_file in config_files:
        validate_and_send(self, config_file)