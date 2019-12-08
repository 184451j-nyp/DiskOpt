from algorithm import DiskParameter, DiskOptimization


class Look:
    def __init__(self):
        self.dp = DiskParameter.DiskParameter('diskq1')
        self.seq = []
        self.distance = 0
        self.direction = "left"
        if self.dp.getPrevious() < self.dp.getCurrent():
            self.direction = "right"
        self.arrangeSeq()
        self.calculateDistance()

    def arrangeSeq(self):
        pos = 0
        initialSeq = self.dp.getSequence()
        initialSeq.sort()
        for i in range(len(initialSeq)):
            if self.dp.getCurrent() < initialSeq[i]:
                initialSeq.insert(i, self.dp.getCurrent())
                pos = i
                break
        if self.direction == "left":
            self.seq = initialSeq[pos-1::-1] + initialSeq[pos:]
        else:
            self.seq = initialSeq[pos:]  + initialSeq[pos-1::-1]
        print("Order of Access: {}".format(self.seq))

    def calculateDistance(self):
        for i in range(len(self.seq)-1):
            self.distance += abs(self.seq[i] - self.seq[i+1])