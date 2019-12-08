from algorithm import DiskParameter

class CSCANAlgorithm:
    def __init__(self):
        self.dp = DiskParameter.DiskParameter("diskq", "diskq6")
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

    def arrangeCSCAN(self, curr, seq, highestValue):
        temp = seq[:]
        CSCAN = []
        n = len(temp)

        def moveToLargest():
            for i in temp:
                if curr < i < highestValue:
                    # current value smaller than the next value and the cylinder value, append it to list CSCAN
                    CSCAN.append(i)

                    # from the opposite, values in temp which is smaller than the current, append it to list CSCAN
                if curr > i >= 0:
                    CSCAN.append(i)
            seq.sort()  # once those value are appended, sort them out in ascending order




        if highestValue > temp[n-1]: # when cylinder value is larger than last value in list seq, append it to list
            temp.append(highestValue)
            moveToLargest()


    def generateCSCAN(self):
        seq = self.dp.getSequence()
        curr = self.dp.getCurrent()
        highestValue = self.dp.getCylinders()

        self.printSequence("CSCAN - Tutorial 4 qn", self.arrangeCSCAN(curr, seq, highestValue))
