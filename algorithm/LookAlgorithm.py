from algorithm import DiskParameter


class Look:
    def __init__(self):
        self.dp = DiskParameter.DiskParameter('diskq1')
        self.seq = []
        self.direction = "left"
        if self.dp.getPrevious() < self.dp.getCurrent():
            self.direction = "right"
        self.arrangeSeq()
        self.printSequence()

    # arranges the given sequence to order of access
    def arrangeSeq(self):
        pos = 0
        initialSeq = self.dp.getSequence()
        initialSeq.sort() # sorts given sequence in ascending order
        for i in range(len(initialSeq)): # inserts current cylinder into sequence
            if self.dp.getCurrent() < initialSeq[i]:
                initialSeq.insert(i, self.dp.getCurrent())
                pos = i
                break
        # arrange sequence accordingly depending on head direction
        if self.direction == "left":
            self.seq = initialSeq[pos-1::-1] + initialSeq[pos:]
        else:
            self.seq = initialSeq[pos:]  + initialSeq[pos-1::-1]
        self.seq.remove(self.dp.getCurrent()) # removes current cylinder from sequence

    # calculates the distance travelled by disk head (taken from DiskOptimization.py)
    def printSequence(self):
        curr = 0
        prev = self.dp.getCurrent()
        total = 0
        working1 = ""
        working2 = ""
        order = ""
        for i in self.seq:
            curr = i
            total += abs(prev - curr)
            working1 += "|" + str(prev) + "-" + str(curr) + "|+"
            working2 += str(abs(prev - curr)) + "+"
            prev = i

        working1 = working1[0:-1]
        working2 = working2[0:-1]
        order = str(self.dp.getCurrent()) + ", " + str(self.seq)[1:-1]
        print("LOOK\n====")
        print("Order of Access: " + order)
        print("Total distance: " + "\n" + working1 + "\n")
        print("= " + working2 + "\n")
        print("= " + str(total) + "\n")
