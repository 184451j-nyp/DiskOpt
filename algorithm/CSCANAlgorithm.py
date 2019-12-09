from algorithm import DiskParameter

class CSCANAlgorithm:
    def __init__(self):
        self.dp = DiskParameter.DiskParameter("diskq1")
        self.generateAnalysis()

    def generateAnalysis(self):
        self.generateCSCAN()

    def printSequence(self, name, location):
        curr = 0
        prev = self.dp.getCurrent()
        total = 0
        working1 = ""
        working2 = ""
        order = ""
        for i in location:
            curr = i
            total += abs(prev - curr)
            working1 += "|" + str(prev) + "-" + str(curr) + "|+"
            working2 += str(abs(prev - curr)) + "+"
            prev = i

        working1 = working1[0:-1]
        working2 = working2[0:-1]
        order = str(self.dp.getCurrent()) + ", " + str(location)[1:-1]
        print(name + "\n====")
        print("Order of Access: " + order)
        print("Total distance: " + "\n" + working1 + "\n")
        print("= " + working2 + "\n")
        print("= " + str(total) + "\n")

    def arrangeCSCAN(self, curr, seq, maxcyn, prev):
        temp = seq[:]
        CSCAN = []
        diff = curr - prev  # to determine which direction its heading

        def moveTowardsLarge():
            for i in temp:
                if curr < i <= maxcyn:
                    CSCAN.append(i)
                    # current value smaller than the next value and the cylinder value, append it to list CSCAN
            for i in temp:
                if curr > i >= 0:
                    CSCAN.append(i)

        def moveTowardSmall():
            for i in reversed(temp):
                if curr > i >= 0:
                    CSCAN.append(i)
            for i in reversed(temp):
                if curr < i <= maxcyn:
                    # current value smaller than the next value and the cylinder value, append it to list CSCAN
                    CSCAN.append(i)

                    # from the opposite, values in temp which is smaller than the current, append it to list CSCAN

        if diff > 0:
            temp.append(maxcyn - 1)  # adding the cylinder value to list seq
            temp.insert(0, 0)
            temp.sort()
            moveTowardsLarge()
            # if difference is bigger than 0, it is heading towards cylinder value

        else:
            temp.append(maxcyn - 1)  # adding the cylinder value to list seq
            temp.insert(0, 0)
            temp.sort()
            moveTowardSmall()
            # if difference is smaller than 0, moving towards the smaller value at the start

        return CSCAN

    def generateCSCAN(self):
        seq = self.dp.getSequence()
        curr = self.dp.getCurrent() # starting value aka current value
        maxcyn = self.dp.getCylinders() # ending value aka cylinder value
        prev = self.dp.getPrevious()
        self.printSequence("CSCAN - Tutorial 4 qn", self.arrangeCSCAN(curr, seq, maxcyn, prev))
