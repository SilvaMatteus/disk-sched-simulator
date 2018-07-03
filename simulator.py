''' Disk scheduling simulator.
'''

from disk_controller import *
from disk_request import Request

class Engine(object):
    def __init__(self, request_list)
        self.__request_list = request_list

    def start(self):
        # Init a disk. Init the controller.
        # Count time by minimal unit and send the update to the controller.
        pass


def load_requests_from_file():
    pass

def plot_stuff():
    pass

if __name__ == '__main__':
    requests = load_requests_from_file()
    engine = Engine(requests)
    engine.start()
    plot_stuff()
