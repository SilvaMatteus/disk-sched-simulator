''' Disk scheduling simulator.
'''

from conf import READING_OPERATION, WRITING_OPERATION, MINIMAL_TIME_UNIT, MAX_TIME_STEP
from disk_controller import *
from disk import Disk
from disk_request import Request
from random import randint

class Engine(object):
    def __init__(self, request_list):
        self.__request_list = sorted(request_list, key=lambda r: r.timestamp)

    def start(self):
        # Init a disk. Init the controller.
        # Count time by minimal unit and send the update to the controller.
        hard_disk = Disk()
        controller = BasicDiskController(hard_disk)
        # timeline
        timestamp = self.__request_list[0].timestamp
        while self.__request_list:
            if self.__request_list[0].timestamp == timestamp:
                print self.__request_list[0]
                controller.receive_new_request(self.__request_list.pop(0))
            controller.time_update(timestamp)
            timestamp += MINIMAL_TIME_UNIT

def convert_line(item):
    if item == 'R':
        return READING_OPERATION
    elif item == 'W':
        return WRITING_OPERATION
    else:
        if '.' in item:
            return int(item.replace('.', '')[:-3])
        else:
            return int(item)

def load_requests_from_file():
    requests = []
    with open('data/systor17-traces-sample.csv', 'r') as file_:
        lines = file_.readlines()
        lines.pop(0) # Discart header.
        for line in lines:
            # timestamp, io_type, offset, size
            line = map(convert_line, line.split(','))
            req = Request(line[0], line[2], line[4], line[5])
            requests.append(req)
    return requests

def plot_stuff():
    pass

if __name__ == '__main__':
    requests = load_requests_from_file()
    engine = Engine(requests)
    engine.start()
    plot_stuff()
