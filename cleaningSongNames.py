import os
from string import digits

base_dir_r = r'C:\Users\shrip\OneDrive\Music\\'
base_dir_w = r'C:\Users\shrip\Pictures\url_downloads\SwaTest\\'

def read_songs(dir_to_r):

    i = 0

    song_names_dict = {}
    song_names = []
    for root, dirs, files in os.walk(dir_to_r, topdown=True):
        for filenames in files:
            filepath = os.path.join(root, filenames)
            song_names.append(filenames)
            b, ext = os.path.splitext(filepath)

            if str(ext) != '.jpg':
                song_names_dict[filenames] = filepath
                #file_w.write('\n')
                #file_w.write(ext)
    #file_w.close()


    clean_names(song_names_dict)

clean_name_map = {}

def clean_names(song_names_dict):

    for k in song_names_dict.keys():
        x,y = os.path.splitext(k)
        #Remove numbers
        x = x.lower().translate({ord(c): None for c in '0123456789'})
        #Replace '_' with spaces
        x = x.translate({ord(c): 32 for c in '_'})
        z =' '.join((x + y).split())
        clean_name_map[k] = z
        print('--> ',x)
    writ_to_file(clean_name_map)

def writ_to_file(song_names_dict):
    fil_to_w_dir = base_dir_w + 'all_songs.txt'
    file_w = open(fil_to_w_dir, 'w')
    file_w.write('\n---------------------------------------------------------------------------- \n \n')
    for k,v in song_names_dict.items():
        file_w.write('key :')
        file_w.write(k)
        file_w.write(' | ')
        file_w.write('val: ')
        file_w.write(v)
        file_w.write('\n')
    file_w.close()


read_songs(base_dir_r)




