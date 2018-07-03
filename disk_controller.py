''' Disk Controller
    You must to implement your own disk controller extending the BasicDiskController.
'''

from conf import MININAL_TIME_UNIT

class BasicDiskController(object):
    def __init__(self, disk):
        self.disk = disk
        self.operation_req_queue = []
        self.initial_time = 0.

    def receive_new_request(self, request):
        self.operation_req_queue.append(request)

    def time_update()
        self.initial_time += MININAL_TIME_UNIT
        # Make the decision whether or not to perform the operation on disk
