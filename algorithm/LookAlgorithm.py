from algorithm import DiskParameter


class Look:
    def __init__(self):
        self.dp = DiskParameter.DiskParameter("diskq.ini", "diskq1")
        self.seq = []
        self.distance = 0
        self.direction = "right"
        if self.dp.getPrevious() > self.dp.getCurrent():
            self.direction = "left"

    def arrangeSeq(self):
        initialSeq = self.dp.getSequence().sort()
        