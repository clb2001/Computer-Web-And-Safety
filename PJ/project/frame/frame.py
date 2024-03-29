from ref import crc16


class FRAME:
    def __init__(self, seq_num, data=b''):
        self.seq = seq_num
        self.data = data
        self.crc = crc16.crc16xmodem(data)
        self.start_time = -1

    def __str__(self):
        return "frame"