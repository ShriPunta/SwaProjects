from itertools import islice

base_file = ""#InputfileName
out_file = ""#OutPutfileName

with open(base_file,'r') as fin, open(out_file, 'w') as fout:
    fout.writelines(islice(fin, 1, None, 8))
