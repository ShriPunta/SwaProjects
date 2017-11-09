import os
import glob

base_dir_r = r'C:\Users\shrip\OneDrive\Music\\'
def call_for_count(files):
    i = i+1
    print(files)
    print(i + '\n')

print(glob.glob(base_dir_r + '\\.txt'))

arr = next(os.walk(base_dir_r))
print(arr)

brr = []
for root,dirs,files in os.walk(base_dir_r,topdown=True):
    for filename in files:
        x,y = (os.path.splitext(filename))
        brr.append(x)

print(brr)