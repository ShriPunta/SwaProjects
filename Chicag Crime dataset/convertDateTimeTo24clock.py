import pandas as pd

base_file = ""#BaseFileName
out_file = ""#OutPutfile

df = pd.read_csv(base_file, index_col="IUCR")

print("000000")



for index, row in df.iterrows():

   splitted = row['Date'].split(' ')

   splitted[0] = pd.to_datetime(splitted[1] + splitted[2]).strftime('%H')
   try:
       df.set_value(index, 'Date',splitted[0])
   except:
       continue


#df.join(df['Date'].str.split('-', 1, expand=True).rename(columns={0:'Date', 1:'Time'}))

try:
    df.to_csv(out_file, sep=',', encoding='utf-8')
except:
    exit(0)
'''
with open(base_file,'r') as fin, open(out_file, 'w') as fout:
    fout.writelines(islice(fin, 1, None, 2))
'''