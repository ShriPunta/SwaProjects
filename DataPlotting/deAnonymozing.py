import time
import os
import pandas as pd
import DataPlotting.UltimateCounter as coun
base_dir = ''
write_dir = ''
all_files_in_dir = []
formatted_filenames = []
globalCounta = coun.N_Counter
error_file_names = []
root_var_dir = r'C:/Users/shrip/Documents/data/Anonymized/variables/'


def fill_list_with_fileNames(pathName):
    for root, dirs, files in os.walk(pathName, topdown=True):
        for filename in files:
            if filename[-3:]==('csv') or filename[-4:]==('xlsx'):
                all_files_in_dir.append(os.path.join(root, filename))
            else:
                continue

def fill_base_paths(variable_name,file_path):
    global base_dir,write_dir

    print(file_path)
    print(variable_name)
    if variable_name=='base_dir':
        file_point=open(file_path,'r')
        base_dir=str(file_point.readline()).strip()
        file_point.close()
    elif variable_name=='write_dir':
        file_point = open(file_path, 'r')
        write_dir = str(file_point.readline()).strip()
        file_point.close()

def start_anonymozing():
    fill_base_paths('base_dir', root_var_dir+'base_dir.txt')
    fill_base_paths('write_dir', root_var_dir+'dir_to_write.txt')
    print('--->',base_dir)
    print('===>',write_dir)
    fill_list_with_fileNames(base_dir)
    print("Anon 22",globalCounta.currentCount)
    globalCounta.resetToOne()
    print("Anon 24",globalCounta.currentCount)
    for each_file_name in all_files_in_dir:
        openAndCopyEachFile(each_file_name)
        break
    print(error_file_names)

def openAndCopyEachFile(fileName):
    globalCounta.getCurrentCount()
    print("Anon 32",globalCounta.currentCount)
    name,ext = os.path.splitext(os.path.basename(fileName))
    currYear = int(name[-4:])
    split_name = '_'.join(str(x) for x in name.split('_')[-2:])
    getAttribs = ['ID', 'DOB', 'Country', 'Career','Gender', 'AdmitType']
    try:
        dataf = pd.read_csv(fileName, skipinitialspace=True, usecols=getAttribs)
        new_columns = dataf.columns.values;
        new_columns[0] = 'UID';
        dataf.columns = new_columns
        for i,row in dataf.iterrows():
            dataf.set_value(i, 'UID', globalCounta.currentCount)
            #dataf.at[i,'UID'] = globalCounta.currentCount
            globalCounta.currentCount+=1
        dataf.to_csv(write_dir + split_name+ext, sep=',',index=False)
        print(dataf.head())
        globalCounta.setNewCount()
    except UnicodeDecodeError:
        error_file_names.append(split_name)

if __name__ == '__main__':
    start_time = time.time()
    start_anonymozing()
    print("---%s seconds --"%(time.time() - start_time))