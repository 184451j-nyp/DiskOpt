from algorithm import DiskParameter


class SSTFAlgorithm:
    def __init__(self):
        self.dp = DiskParameter.DiskParameter("diskq1")
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
            total += abs(prev-curr)
            working1 += "|" + str(prev) + "-" + str(curr) + "|+"
            working2 += str(abs(prev-curr)) + "+"
            prev = i

        working1 = working1[0:-1]
        working2 = working2[0:-1]
        order = str(self.dp.getCurrent())+", "+str(location)[1:-1]
        print(name+"\n====")
        print("Order of Access: " + order)
        print("Total distance: " + "\n" + working1 + "\n")
        print("= " + working2 + "\n")
        print("= " + str(total) + "\n")

    def arrangeSSTF(self, curr, seq):
        temp = seq[:]
        sstf = []
        temp2 = temp[:]
        num = curr
        for i in temp:
            minimum = max(seq)
            num2 = num
            # looping through the list seq
            # defining the largest value in list seq as var minimum
            # var num2 as the current value
            for ii in temp2:
                dist = abs(num2 - ii)
                # finding the distance between current value and iterated value from for loop
                if dist < minimum:
                    num = ii
                    minimum = dist
                # if the distance is smaller than the current largest value, current value becomes the iterated value
                # minimum value become the value of distance
            temp2.remove(num)
            sstf.append(num)
        return sstf
        # remove the current number from the list temp2, append to list and return

    def generateSSTF(self):
        seq = self.dp.getSequence()  # achieving the sequence
        curr = self.dp.getCurrent()  # achieving the current value
        self.printSequence("SSTF", self.arrangeSSTF(curr, seq))

    def generateAnalysis(self):
        self.generateSSTF()
        # execute the SSTF method