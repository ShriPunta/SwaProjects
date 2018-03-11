import csv

class CreateDictFromCSV:
    filePathToRead = ''
    header = []
    pathToHeaderFile = ''
    listOfMaps = list(dict())
    def __init__(self,pathToRead,inputPathToHeaderFile):
        print("Entered")
        self.populateHeader(inputPathToHeaderFile)
        listOfMaps = self.readCSV(pathToRead)

    def populateHeader(self,pathToHeaderFile):
        fp = open(pathToHeaderFile, newline='')
        reader = csv.reader(fp)
        header = next(reader)
        print(header)
        fp.close()

    def readCSV(self,pathToRead):
        '''reader = csv.reader(open('filename.csv', 'r'))
        for k, v in reader:
            tempDict = dict()
            tempDict[k] = v

        return self.listOfMaps'''
        with open(pathToRead, mode='r') as infile:
            reader = csv.reader(infile)
            for line in reader:
                for cell in line:
                    tempDict = dict()



            #writer = csv.writer(outfile)
            #mydict = {rows[0]: rows[1] for rows in reader}

cooro = CreateDictFromCSV(r"C:\Users\shrip\Pictures\url_downloads\crawler download\corro.csv")