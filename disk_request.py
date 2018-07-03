class Request(object):
    def __init__(self, timestamp, io_type, offset, size):
        self.timestamp = timestamp
        self.io_type = io_type
        self.offset = offset
        self.size = size

    def __str__(self):
        return str(self.__dict__)
