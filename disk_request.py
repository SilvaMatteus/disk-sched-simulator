from conf import READING_OPERATION, WRITING_OPERATION

class Request(object):
    def __init__(self, timestamp, io_type, offset, size):
        self.timestamp = timestamp
        self.io_type = READING_OPERATION
        self.offset = offset
        self.size = size
