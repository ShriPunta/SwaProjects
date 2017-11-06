import os

base_dir = r'C:\Users\shrip\Pictures\url_downloads\\'

read_dir = base_dir+r"test\\"

def enter_dir(curr_filepath):
    print(curr_filepath)
    for root, dirs, files in os.walk(curr_filepath, topdown=False):
      for filename in files:
        filepath = os.path.join(root,filename)
        print(filepath)
        b,ext = os.path.splitext(filepath)
        print(ext)
        #print(b)

        ind = filepath.find('.')
        print(ind)
        if ext == ".plt":
            os.rename(filepath,filepath[0:ind]+".txt")
            print('-----------')
            return
        elif ext == ".txt":
            os.rename(filepath, filepath[0:ind] + ".csv")
            print('-#####-')
            return
    return

def show_menu():
        i=10
        while i<1:
            print("Hey Please choose your the type of file you wish to read:")
            print("1: .plt")
            print("2: .txt")
            print("0 to exit")

            try:
                i = int(input("Enter a numerical value for the given choices"))
            except:
                print("Thats not a valid input")
                print("Try Again!!!")


show_menu()
enter_dir(read_dir)
