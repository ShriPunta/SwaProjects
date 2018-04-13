import os
import pandas as pd
import DataPlotting.UltimateCounter as coun
base_dir = r'C:/Users/shrip/Documents/data/Anonymized'
all_files_in_dir = []
formatted_filenames = []
globalCounta = coun.N_Counter

def fill_list_with_fileNames(pathName):
    for root, dirs, files in os.walk(pathName, topdown=True):
        for filename in files:
            if filename[-3:]!='csv':
                continue
            all_files_in_dir.append(os.path.join(root, filename))

def start_anonymozing():
    fill_list_with_fileNames(base_dir)
    for each_file_name in all_files_in_dir:
        openAndCopyEachFile(each_file_name)

def openAndCopyEachFile(fileName):
    name,ext = os.path.splitext(os.path.basename(fileName))
    getAttribs = ['ID','DOB','Country','Gender','AdmitType']
    split_name = '_'.join(str(x) for x in name.split('_')[-2:])
    split_name.join(ext)
    print(split_name)

    #dataf = pd.read_csv(fileName, skipinitialspace=True, usecols=getAttribs,nrows=500)
    print(globalCounta.currentCount)
    print(globalCounta.currentCount)
    globalCounta.currentCount += 1
    globalCounta.currentCount += 1
    globalCounta.currentCount += 1
    print(globalCounta.currentCount)
    print(globalCounta.currentCount)


if __name__ == '__main__':
    start_anonymozing()