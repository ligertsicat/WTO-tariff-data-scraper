import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import os



path = '.'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.xls' in file:
            files.append(os.path.join(r, file))




df = pd.read_excel('File.xlsx', sheet_name='Bound', skiprows=[0,1,2,3])


for f in files:
    print(f[2:])

    df2 = pd.read_excel(f[2:], sheet_name='Bound', skiprows=[0,1,2,3])

    bigdata = df.append(df2)

exit()


df = pd.read_excel('File.xlsx', sheet_name='Bound', skiprows=[0,1,2,3])


df2 = pd.read_excel('DataExport_18_8_2019__5_56_54.xls', sheet_name='Bound', skiprows=[0,1,2,3])


print(df.head())
print(df2.head())

bigdata = df.append(df2)

print(bigdata)

bigdata.to_csv(r'a.csv')