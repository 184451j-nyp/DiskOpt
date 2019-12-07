from algorithm import DiskParameter


class DiskOptimization:
    def __init__(self):
        self.dp = DiskParameter.DiskParameter("diskq1.ini", "diskq1")
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
            for ii in temp2:
                dist = abs(num2 - ii)
                # print("DIST:" + str(dist))
                if dist < minimum:
                    num = ii
                    minimum = dist
                    # print("*here")
            # print("--------------STOP " + str(num) + "---------------")
            temp2.remove(num)
            sstf.append(num)
        return sstf
    
        def arrangeSCAN(self, curr, seq, prev, maxcyn):
        temp = seq[:]
        SCAN = []
        temp2 = seq[:]
        n = len(temp)
        temp2.append(curr)
        temp2.sort()

        diff = curr - prev # check if its going left or right
        if diff > 0:
            direction = "RIGHT"
            if maxcyn != 0 and maxcyn > temp2[n - 1]:
                temp2.append(maxcyn - 1) # append max cylinder number to list
        else:
            direction = "LEFT"
            temp2.append(0) # append minimum cylinder number to list
            temp2.sort()

        index = temp2.index(curr)
        if direction =="RIGHT":
            for i in temp2:
                if temp2[index] < i < maxcyn: # find values bigger than current and smaller than maximum cylinder
                    SCAN.append(i) # if found, append to created empty list

            for i in reversed(temp2):
                if temp2[index] > i >= 0: # find values staller than current and bigger than smallest cylinder
                    SCAN.append(i) # if found, append to created empty list

        if direction == "LEFT":
            for i in reversed(temp2):
                if temp2[index] > i >= 0: # find values staller than current and bigger than smallest cylinder
                    SCAN.append(i) # if found, append to created empty list

            for i in temp2:
                if temp2[index] < i < maxcyn: # find values bigger than current and smaller than maximum cylinder
                    SCAN.append(i) # if found, append to created empty list

        return SCAN

    def generateFCFS(self):
        seq = self.dp.getSequence()
        self.printSequence("FCFS", seq)

    def generateSSTF(self):
        seq = self.dp.getSequence()
        curr = self.dp.getCurrent()
        self.printSequence("SSTF", self.arrangeSSTF(curr, seq))

    def generateAnalysis(self):
        self.generateFCFS()
        self.generateSSTF()
        self.gemerateSCAN()
