# dtctl
This cli is a work in progress. The goal is a straightforward way to control Dynatrace configurations in a fashion similar to and inspired by Kubernetes' kubectl. Hopefully this will make some tedious administrative tasks faster as well as demonstrate a way that you can store configuration files outside of Dynatrace. Right now you interact with all configs as YAML, they get converted to and from JSON when interacting with the API.

To use you must have Python 3.6+ installed as well as the requirements specified in requirements.txt.

This is based on Google's Fire module for creating CLI tools in Python.

## Config file
Supply your config in a yaml file dtctl.yaml with the following entries:
```
token: <token>
tenant:<environment location e.g.-> https://blablabla.sprint.dynatracelabs.com>
defaultApiVersion: v1
```
## Usage
General usage will be python dtctl.py <endpoint> <operation> [\<config or entity id>]
### Supported operations
Currently the following operations are supported for the supported endpoints (see next section):
* list
  - Returns the name and id of all of the relevant configs/rules
  - python dtctl.py management-zones list
* describe <id>
  - Returns the configuration for a given config rule in YAML format (can be piped to a file for storage or modification)
  - python dtctl.py alerting-profiles describe fb5b38f5-4f6e-48e5-86e5-2148808cb1f2
* create <example.yaml>[, <example_2.yaml>] or directory=(/directory)
  - either creates a rule using the provided yaml file (or series of files) or if the --directory= option is used creates rules for all of the files in that directory
  - python dtctl.py notifications create example.yaml
  - python dtctl.py notifications create example.yaml example_2.yaml
  - python dtctl.py notifications create --directory=/myconfigs/tocreate
  - try "getting" a config to see what these yaml files can look like for different config types / endpoints
* update config_id example.yaml
  - updates the config rule specified by id with the supplied yaml file
  - python dtctl.py alerting-profiles update 49e329e5-4a04-4e21-b7b4-3c748589be16 example.yaml
* delete config_id [, <config_id_2>]
  - deletes the rules specified by id
  - python dtctl.py dashboards delete dc645c2a-038f-4f75-8981-b59b5c1d3f33
  - python dtctl.py dashboards delete dc645c2a-038f-4f75-8981-b59b5c1d3f33 e366354a-7cea-42a0-ae06-4d4244f0f103
  
  ### Supported endpoints
  * alerting-profiles
  * auto-tags
  * dashboards
  * maintenance-windows
  * management-zones
  * notfications (problem notifications)
  * web-applications
    - for now use describe-privacy or update-privacy when working with data privacy rules for a web app
  * cluster
    - options for the cluster endpoint are:
      - python dtctl.py cluster version
      - python dtctl.py cluster time
