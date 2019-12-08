from algorithm import DiskParameter


class DiskOptimization:
    def __init__(self):
        self.dp = DiskParameter.DiskParameter("diskq1")
        self.dp3 = DiskParameter.DiskParameter("diskq3") # get perimeters from diskq3 in diskq.ini
        self.dp4 = DiskParameter.DiskParameter("diskq4") # get perimeters from diskq4 in diskq.ini
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

    def arrangeSCAN(self, curr, seq, prev, maxcyn):

        temp = seq[:]
        SCAN = []
        n = len(temp)

        def left(): # move disk head Right
            for i in reversed(temp):
                if curr > i >= 0: # find values smaller than current and equal to or bigger than smallest cylinder
                    SCAN.append(i) # if found, append to created empty list

        def right(): # move disk head Left
            for i in temp:
                if curr < i < maxcyn: # find values bigger than current and smaller than maximum cylinder
                    SCAN.append(i) # if found, append to created empty list

        diff = curr - prev # check if its going left or right
        if diff > 0:
            if maxcyn != 0 and maxcyn > temp[n - 1]:
                temp.append(maxcyn - 1) # append max cylinder number to list
                temp.sort()
                right()
                left()

        else:
            temp.append(0) # append minimum cylinder number to list
            temp.sort()
            left()
            right()

        return SCAN

    def generateFCFS(self):
        seq = self.dp.getSequence()
        self.printSequence("FCFS", seq)

    def generateSCAN(self):
        seq = self.dp3.getSequence()
        curr = self.dp3.getCurrent()
        prev = self.dp3.getPrevious()
        maxcyn = self.dp3.getCylinders()
        self.printSequence("SCAN - Right then left", self.arrangeSCAN(curr, seq, prev, maxcyn))
        seq = self.dp4.getSequence()
        curr = self.dp4.getCurrent()
        prev = self.dp4.getPrevious()
        maxcyn = self.dp4.getCylinders()
        self.printSequence("SCAN - Left then right", self.arrangeSCAN(curr, seq, prev, maxcyn))

    def generateLook(self):
        seq = []
        direction = "left"
        if self.dp.getPrevious() < self.dp.getCurrent():
            direction = "right"
        pos = 0
        initialSeq = self.dp.getSequence()
        initialSeq.sort()
        for i in range(len(initialSeq)):
            if self.dp.getCurrent() < initialSeq[i]:
                initialSeq.insert(i, self.dp.getCurrent())
                pos = i
                break
        if direction == "left":
            seq = initialSeq[pos - 1::-1] + initialSeq[pos:]
        else:
            seq = initialSeq[pos:] + initialSeq[pos - 1::-1]
        seq.remove(self.dp.getCurrent())
        self.printSequence("LOOK", seq)

    def generateAnalysis(self):
        self.generateFCFS()
        self.generateSCAN()
        self.generateLook()
