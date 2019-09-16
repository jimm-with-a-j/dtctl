# common functions that will essentially be the same across API endpoints
# for any actions specific to those endpoints the work will likely be in that endpoint class

import requests
import yaml
import os


def validate_and_send(self, config_file, config_id=None):
    success = False  # whether or not the change was successfully applied
    try:
        with open(config_file, "r") as file:
            try:
                json_payload = yaml.safe_load(file)
                if validate_config(self, json_payload, config_id) is True:
                    success = apply_config(self, json_payload, config_id)  # returns boolean
            except yaml.YAMLError as exc:
                print("Some issue loading your yaml, please verify it is valid.")
                print(exc)
            except Exception as e:
                print(e)
    except FileNotFoundError as exc:
        print("File {file} could not be found".format(file=config_file))
    except Exception as e:  # catching generic exception (not ideal...)
        print(e)

    return success


def validate_config(self, json_payload, config_id=None):
    is_valid = False
    try:
        # when validating for an existing config id (e.g. an update)
        if config_id is not None:
            validation_response = requests.post(self.endpoint + str(config_id) + '/validator/',
                                                headers=self.config.auth_header, json=json_payload)
        # validating a new configuration (e.g. create)
        if config_id is None:
            validation_response = requests.post(self.endpoint + 'validator/',
                                                headers=self.config.auth_header, json=json_payload)
        if str(validation_response.status_code).startswith('2'):
            is_valid = True
    except Exception as e:
        print(e)
    return is_valid


def apply_config(self, json_payload, config_id=None):
    is_created = False
    if config_id is None:
        response = requests.post(self.endpoint, headers=self.config.auth_header, json=json_payload)
    if config_id is not None:
        response = requests.put(self.endpoint + config_id, headers=self.config.auth_header, json=json_payload)
    if str(response.status_code).startswith('2'):
        print("Success: " + str(response.status_code))
    else:
        print(response.content)
    return is_created


def get_json(self):
    success = False
    response = requests.get(self.endpoint, headers=self.config.auth_header)
    response_json = response.json()
    if str(response.status_code).startswith('2'):
        success = True
    else:
        print("Error calling {target}, response code: {code}".format(target=self.endpoint, code=response.status_code))

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
                print("{config} {id} deleted successfully (response: {code})"
                      .format(config=self.type, id=config_id, code=deletion_response))
            else:
                print("Error returned when deleting profile " + config_id)
        except AssertionError as e:
            print("Config {id} does not exist in the environment".format(id=config_id))


def list(self):
    success, config_list_json = get_json(self)
    if success:
        # some endpoints return something other than 'values'
        if self.type == "Dashboard":
            config_list_json = config_list_json['dashboards']
        else:
            config_list_json = config_list_json['values']
    return config_list_json


def create(self, *config_files, directory=None):
    # when creating specific files
    if directory is None:
        for config_file in config_files:
            validate_and_send(self, config_file)
    # when passed a directory
    if directory is not None:
        configs_in_directory = os.listdir(directory)
        for file in configs_in_directory:
            if file.endswith(".yaml"):
                validate_and_send(self, directory + '/' + file)



