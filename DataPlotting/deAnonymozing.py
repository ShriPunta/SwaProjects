import time
import os
import pandas as pd
import DataPlotting.UltimateCounter as coun
import re
import datetime

base_dir = ''
write_dir = ''
all_files_in_dir = []
formatted_filenames = []
globalCounta = coun.N_Counter
error_file_names = []
root_var_dir = r'C:/Users/shrip/Documents/data/Anonymized/variables/'
start_date_dict = {0:'01,15',1:'01,15',2:'05,15',3:'08,15'}

def fill_list_with_fileNames(pathName):
    for root, dirs, files in os.walk(pathName, topdown=True):
        for filename in files:
            if filename[-3:]==('csv') or filename[-4:]==('xlsx'):
                all_files_in_dir.append(os.path.join(root, filename))
            else:
                continue

def fill_base_paths(variable_name,file_path):
    global base_dir,write_dir
    if variable_name == 'base_dir':
        file_point=open(file_path,'r')
        base_dir=str(file_point.readline()).strip()
        file_point.close()
    elif variable_name == 'write_dir':
        file_point = open(file_path, 'r')
        write_dir = str(file_point.readline()).strip()
        file_point.close()

def start_anonymozing():
    fill_base_paths('base_dir', root_var_dir+'base_dir.txt')
    fill_base_paths('write_dir', root_var_dir+'dir_to_write.txt')
    fill_list_with_fileNames(base_dir)
    globalCounta.resetToOne()
    for each_file_name in all_files_in_dir:
        openAndCopyEachFile(each_file_name)
        break

    print(error_file_names)

def openAndCopyEachFile(fileName):
    globalCounta.getCurrentCount()
    name,ext = os.path.splitext(os.path.basename(fileName))
    dateToCompare = getTheDateToCompare(name)
    split_name = '_'.join(str(x) for x in fileName.split('_')[-2:])


    getAttribs = ['ID', 'DOB', 'Country', 'Career','Gender', 'AdmitType']
    try:
        dataf = pd.read_csv(fileName, skipinitialspace=True, usecols=getAttribs)
        new_columns = dataf.columns.values;
        new_columns[0] = 'UID';
        dataf.columns = new_columns
        for i,row in dataf.iterrows():
            dataf.set_value(i, 'UID', globalCounta.currentCount)
            #dataf.at[i,'UID'] = globalCounta.currentCount

            #age Calculate
            nowIs = datetime.datetime.now()
            date_read = datetime.datetime(int(nowIs.year),int(nowIs.month),int(nowIs.day),0,0,0)

            if str(row['DOB']).find('-') != -1:
                #print("Entered 1")
                date_read = datetime.datetime.strptime(row['DOB'],'%m-%d-%Y')
            elif str(row['DOB']).find('/') != -1:
                #print("Entered 2")
                date_read = datetime.datetime.strptime(row['DOB'],'%m/%d/%Y')

            #print(str(date_read))
            calculated_age = dateToCompare - date_read
            #print(round(calculated_age.days/365))
            dataf.set_value(i, 'age', calculated_age)
            #increase counter
            globalCounta.currentCount+=1

        #dataf.to_csv(write_dir + split_name+ext, sep=',',index=False)
        print(dataf.head())
        globalCounta.setNewCount()
    except UnicodeDecodeError:
        error_file_names.append(split_name)

def getTheDateToCompare(fileName):
    flag=0
    try:
        currYear = int(list(re.findall(r'\d{4}', fileName))[0])
    except:
        currYear = int((datetime.datetime.now()).year)

    if fileName.find('Spr') != '-1':
        flag = 1
    elif fileName.find('Fall') != '-1':
        flag = 3
    elif fileName.find('Summ') != '-1':
        flag = 2

    monthAndDate = [int(x) for x in start_date_dict.get(flag).split(',')]
    formulatedDT = datetime.datetime(currYear, monthAndDate[0], monthAndDate[1], 0, 0, 0)
    print(str(formulatedDT))
    return formulatedDT



if __name__ == '__main__':
    start_time = time.time()
    start_anonymozing()
    print("---%s seconds --"%(time.time() - start_time))