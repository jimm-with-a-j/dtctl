import fire
from endpoints.cluster import Cluster
from config_reader import Config

def sanity():
    return "Sane"


def get(endpoint_class, attribute):
    return


class CLI:
    def __init__(self):
        self.config = Config()
        self.cluster = Cluster(config=self.config)

if __name__ == '__main__':
    fire.Fire(CLI)
