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

    def arrangeCSCAN(self, curr, seq, end, prev):
        temp = seq[:]
        CSCAN = []
        diff = curr - prev  # to determine which direction its heading

        def moveTowardsLarge():
            for i in temp:
                if curr < i <= end:
                    CSCAN.append(i)
                    # current value smaller than the next value (i) and the cylinder value, append it to list CSCAN

            for i in temp:
                if curr > i >= 0:
                    CSCAN.append(i)
                    # current value bigger than the next value (i), append (i) to list CSCAN

        def moveTowardSmall():
            for i in reversed(temp):
                if curr > i >= 0:
                    CSCAN.append(i)
                    # in reverse manner, append the next value (i) to list CSCAN when it is smaller than current value

            for i in reversed(temp):
                if curr < i <= end:
                    CSCAN.append(i)
                    # in reverse manner, append the next value (i) to list CSCAN when it is bigger than current value

        if diff > 0:
            if end != 0:
                temp.append(end)
                # add to list temp if no duplicated var end
            temp.insert(0, 0)
            moveTowardsLarge()
        else:
            temp.append(end)
            temp.insert(0, 0)
            moveTowardSmall()

        return CSCAN

    def generateCSCAN(self):
        seq = self.dp.getSequence()
        curr = self.dp.getCurrent()  # starting value aka current value
        end = self.dp.getCylinders()  # ending value aka cylinder value
        prev = self.dp.getPrevious()
        self.printSequence("CSCAN - lecture qn", self.arrangeCSCAN(curr, seq, end, prev))
