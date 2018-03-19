import csv

class PlayDictAndCSV:
    filePathToRead = ''
    header = []
    pathToHeaderFile = ''
    mapToCSVMap = ''
    listOfMaps = list(dict())
    def __init__(self,pathToRead,inputPathToHeaderFile):
        pass
        print("Entered")
        self.populateHeader(inputPathToHeaderFile)
        print(self.header)
        listOfMaps = self.readCSV(pathToRead)



    def __init__(self,writeMapToCSVpath,mapToCSVMap):
        pass
        print(writeMapToCSVpath)
        self.mapToCSVMap = mapToCSVMap
        self.writeMapToCSV(writeMapToCSVpath)

    def writeMapToCSV(self,writeMapToCSVpath,mapToCSVMap):
        filePathToWrite = r"C:\Users\shrip\Pictures\url_downloads\crawler download" if writeMapToCSVpath!=('' or None) else writeMapToCSVpath
        with open((filePathToWrite + '\\Traversed.csv'), 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in mapToCSVMap.items():
                writer.writerow([str(key), str(value)])

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
