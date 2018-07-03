''' Disk Controller
    You must to implement your own disk controller extending the BasicDiskController.
'''

class BasicDiskController(object):
    def __init__(self, disk):
        self.disk = disk
        self.operation_req_queue = []
        self.timestamp = 0.

    def receive_new_request(self, request):
        self.operation_req_queue.append(request)

    def time_update(self, timestamp):
        self.timestamp = timestamp
        # Make the decision whether or not to perform the operation on disk
