import fire
from endpoints.cluster import Cluster
from endpoints.alerting_profiles import AlertingProfiles
from config_reader import Config


class CLI:
    def __init__(self):
        self.config = Config()
        self.cluster = Cluster(config=self.config)
        self.alerting_profiles = AlertingProfiles(config=self.config)


if __name__ == '__main__':
    fire.Fire(CLI)
