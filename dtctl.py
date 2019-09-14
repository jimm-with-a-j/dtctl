import fire
from endpoints.cluster import Cluster
from endpoints.alerting_profiles import AlertingProfiles
from endpoints.management_zones import ManagementZones
from endpoints.auto_tags import AutoTags
from endpoints.maintenance_windows import MaintenanceWindows
from endpoints.dashboards import Dashboards
from endpoints.notifications import Notifications
from dtctl_modules.config_reader import Config


class CLI:
    def __init__(self):
        self.config = Config()
        self.cluster = Cluster(config=self.config)
        self.alerting_profiles = AlertingProfiles(config=self.config)
        self.management_zones = ManagementZones(config=self.config)
        self.auto_tags = AutoTags(config=self.config)
        self.maintenance_windows = MaintenanceWindows(config=self.config)
        self.dashboards = Dashboards(config=self.config)
        self.notifications = Notifications(config=self.config)


if __name__ == '__main__':
    fire.Fire(CLI)
