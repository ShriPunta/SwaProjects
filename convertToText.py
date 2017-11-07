import os

base_dir = r'C:\Users\shrip\Pictures\url_downloads\test\\'


def enter_dir(curr_filepath):
    print(curr_filepath)
    for root, dirs, files in os.walk(curr_filepath, topdown=True):
      for filename in files:
        filepath = os.path.join(root,filename)
        print(filepath)
        b,ext = os.path.splitext(filepath)
        print(ext)
        #print(b)
        del_start_lines(filepath)

        ind = filepath.find('.')
        print(ind)
        if ext == ".plt":
            os.rename(filepath,filepath[0:ind]+".txt")
            print('-----------')
        elif ext == ".txt":
            os.rename(filepath, filepath[0:ind] + ".csv")
            print('-#####-')
    return

def defin_header():
    return (r"Latitude,Longitude,dele_colum,Altitude,dele_colum,Date,Time")

#delete first 6 lines and a header
def del_start_lines(filename):
    f = open(filename)
    lines = f.readlines()
    f.seek(0,0)

    f = open(filename, 'w')
    f.write(defin_header())
    f.write('\n')
    f.writelines(lines[6:])
    f.close()

enter_dir(base_dir)
