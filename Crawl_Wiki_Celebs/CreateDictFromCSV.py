import csv

class CreateDictFromCSV:
    filePathToRead = ''
    header = []
    pathToHeaderFile = ''
    listOfMaps = list(dict())
    def __init__(self,pathToRead,inputPathToHeaderFile):
        print("Entered")
        self.populateHeader(inputPathToHeaderFile)
        print(self.header)
        listOfMaps = self.readCSV(pathToRead)

    def populateHeader(self,pathToHeaderFile):
        fp = open(pathToHeaderFile, newline='')
        reader = csv.reader(fp)
        self.header = next(reader)
        fp.close()

    def readCSV(self,pathToRead):
        with open(pathToRead, mode='r') as infile:
            reader = csv.reader(infile)
            for line in reader:
                tempDict = dict()
                for cell in line:
                    index = line.index(cell)
                    try:
                        self.header[index]
                    except:
                        print("Not Enough number of parameters")

                    tempDict[self.header[index]] = cell
                self.listOfMaps.append(tempDict)
        return self.listOfMaps

#cooro = CreateDictFromCSV(r"C:\Users\shrip\Pictures\url_downloads\crawler download\corro.csv",r"C:\Users\shrip\Pictures\url_downloads\crawler download\headers.csv")
#print(cooro.listOfMaps)