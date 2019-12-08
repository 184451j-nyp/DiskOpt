from algorithm import DiskParameter


class DiskOptimization:
    def __init__(self):
        self.dp = DiskParameter.DiskParameter("diskq.ini", "diskq4")
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
        temp2 = seq[:]
        n = len(temp)
        temp2.append(curr)
        temp2.sort()

        def left():
            for i in reversed(temp2):
                if temp2[index] > i >= 0: # find values staller than current and bigger than smallest cylinder
                    SCAN.append(i) # if found, append to created empty list

        def right():
            for i in temp2:
                if temp2[index] < i < maxcyn: # find values bigger than current and smaller than maximum cylinder
                    SCAN.append(i) # if found, append to created empty list

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
            right()
            left()

        if direction == "LEFT":
            left()
            right()

        return SCAN

    def generateFCFS(self):
        seq = self.dp.getSequence()
        self.printSequence("FCFS", seq)

    def generateSCAN(self):
        seq = self.dp.getSequence()
        curr = self.dp.getCurrent()
        prev = self.dp.getPrevious()
        maxcyn = self.dp.getCylinders()
        self.printSequence("SCAN", self.arrangeSCAN(curr, seq, prev, maxcyn))


    def generateAnalysis(self):
        self.generateFCFS()
        self.generateSCAN()
