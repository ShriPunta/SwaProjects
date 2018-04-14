class N_Counter:
    currentCount = 0
    counterStorage = 'C:/Users/shrip/Documents/data/Anonymized/variables/ultimateCounter.txt'

    @staticmethod
    def getCurrentCount():
        first_line = ''
        f = open(N_Counter.counterStorage, 'r')
        try:
            N_Counter.currentCount = int(f.readline())
        except ValueError:
            print("Counter File is empty")
            f.close()
            return
        print("Reading 15",N_Counter.currentCount)
        f.close()
        print("Reading 17",N_Counter.currentCount)

    @staticmethod
    def setNewCount():
        f = open(N_Counter.counterStorage,'w')
        f.write(str(N_Counter.currentCount))
        f.close()

    @staticmethod
    def resetToOne():
        first_line = ''
        f = open(N_Counter.counterStorage, 'w+')
        try:
            cont = int(f.readline())
        except ValueError:
            print("Counter File is Empty")
            return
        if(cont != 1):
            print("Resetting",N_Counter.currentCount)
            N_Counter.currentCount=1
            f.write('1')
        f.close()




