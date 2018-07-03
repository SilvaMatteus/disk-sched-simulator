from conf import *

class Disk():
    def __init__(self):
        self.__blocks = []
        self.__offset = 0
        self.__usage_time = 0.

    def get_position(self):
        return self.__offset

    def access(self, offset, num_of_bytes, operation):
        response_time = abs(self.__offset - offset) * DELAY_TO_MOVE
        num_of_blocks = (math.ceil(num_of_bytes/float(BLOCK_SIZE)))
        if operation == READING_OPERATION:
            response_time += DELAY_TO_R * num_of_blocks
        elif operation == WRITING_OPERATION:
            response_time += DELAY_TO_W * num_of_blocks
        else:
            raise ValueError('Operation not recognized!')
        self.__offset = offset
        self.__usage_time += response_time
        print 'Total usage: [ %f ]' % self.__usage_time
        return response_time
