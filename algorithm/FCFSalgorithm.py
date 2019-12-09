from algorithm import DiskParameter


class FcFs:
    def __init__(self):
        self.dp = DiskParameter.DiskParameter("diskq2")
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

        working2 = working2[0:-1]
        working1 = working1[0:-1]
        order = str(self.dp.getCurrent()) + ", " + str(location)[1:-1]
        print(name + "\n====")
        print("Order of Access: " + order)
        print("Total distance: " + "\n" + working1 + "\n")
        print("= " + working2 + "\n")
        print("= " + str(total) + "\n")

    def generateFCFS(self):
        seq = self.dp.getSequence()
        self.printSequence("FCFS", seq)

    def generateAnalysis(self):
        self.generateFCFS()