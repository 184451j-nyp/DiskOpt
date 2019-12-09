from algorithm import DiskParameter


class CSCANAlgorithm:
    def __init__(self):
        self.dp = DiskParameter.DiskParameter("diskq7")
        self.generateAnalysis()

    def generateAnalysis(self):
        self.generateAnalysis()

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

    def arrangeCSCAN(self, curr, seq, end):
        temp = seq[:]
        CSCAN = []
        start = temp[0]  # first value in list seq
        prev = self.dp.getPrevious()
        n = len(temp)
        diff = curr - prev  # to determine which direction its heading

        def moveTowardsLarge():
            for i in temp:
                if curr < i < end:
                    # current value smaller than the next value and the cylinder value, append it to list CSCAN
                    CSCAN.append(i)

        def moveTowardSmall():
            for i in temp:
                if curr > i >= 0:
                    CSCAN.append(i)

                    # from the opposite, values in temp which is smaller than the current, append it to list CSCAN

        if diff > 0:
            if end != 0 and end > temp[n - 1]:
                temp.append(end)  # adding the cylinder value to list seq
                temp.sort()  # sorting list seq to ascending order
                moveTowardsLarge()
                moveTowardSmall()

            else:
                temp.append(start)
                temp.sort()
                moveTowardSmall()
                moveTowardsLarge()

        return CSCAN

    def generateCSCAN(self):
        seq = self.dp.getSequence()
        curr = self.dp.getCurrent()  # starting value aka current value
        end = self.dp.getCylinders()  # ending value aka cylinder value

        self.printSequence("CSCAN - Tutorial 4 qn", self.arrangeCSCAN(curr, seq, end))
