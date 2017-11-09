import os

base_dir_r = r'C:\Users\shrip\OneDrive\Music\\'
base_dir_w = r'C:\Users\shrip\Pictures\url_downloads\SwaTest\\'

def read_names(dir_to_r):
    fil_to_w_dir = base_dir_w + 'all_songs.txt'

    file_w = open(fil_to_w_dir, 'w')
    file_w.write('\n---------------------------------------------------------------------------- \n \n')
    for root, dirs, files in os.walk(dir_to_r, topdown=True):

        for filenames in files:
            filepath = os.path.join(root, filenames)

            b, ext = os.path.splitext(filepath)

            if ext is not 'jpg':

                file_w.write('\n')
                file_w.write(filenames)

read_names(base_dir_r)




