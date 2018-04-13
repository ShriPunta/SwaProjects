class N_Counter:
    currentCount = 0
    counterStorage = 'C:/Users/shrip/Documents/data/Anonymized/ultimateCounter.txt'

    @staticmethod
    def getCurrentCount():
        first_line = ''
        f = open(N_Counter.counterStorage, 'r')
        N_Counter.currentCount = int(f.readline())
        f.close()

    @staticmethod
    def setNewCount():
        f = open(N_Counter.counterStorage,'w')
        f.write(N_Counter.currentCount)
        f.close()


