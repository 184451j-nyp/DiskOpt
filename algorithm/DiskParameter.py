import configparser


class DiskParameter:
    def __init__(self, filename, section):
        Config = configparser.ConfigParser()
        Config.read(str(filename))
        self.cylinders = Config.getint(section, 'cylinders')
        self.previous = Config.getint(section, 'previous')
        self.current = Config.getint(section, 'current')
        self.sequence = Config.get(section, 'sequence')
        self.sequence = self.sequence.split(",")
        seq = []
        for i in self.sequence:
            seq.append(int(i))
            self.sequence = seq

    def getCylinders(self):
        return self.cylinders

    def getPrevious(self):
        return self.previous

    def getCurrent(self):
        return self.current

    def getSequence(self):
        return self.sequence