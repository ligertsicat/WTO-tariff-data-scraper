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


sheets = ['Bound', 'HS_Concordance', 'Applied_MFN', 'Applied_NonMFN', 'NonMFN_Only_Partners']

for sheet in sheets:
	df = pd.DataFrame()

	for f in files:
	    print(f[2:])

	    try:
	    	d = pd.read_excel(f[2:], sheet_name=sheet, skiprows=[0,1,2,3])
	    	df = df.append(d)
	    except:
	    	continue

	filename=sheet+".csv"
	df.to_csv(filename, index=False, header=False)


#bigdata.to_csv(r'a.csv')
