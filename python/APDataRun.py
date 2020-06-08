import os
import pandas as pd
import numpy as np

file_path = '../data/XTAL_Challange.xlsx'

xl = pd.ExcelFile(file_path)

sheetname = xl.sheet_names[2]

nrows = 10

# currency = pd.read_excel(file_path, sheet_name=0, skiprows=1)

xrate = pd.read_excel(file_path, sheet_name=2, skiprows=0, nrows=nrows)

values = pd.read_excel(file_path, sheet_name=1, skiprows=0, nrows=nrows)

temp = np.zeros((7, 1))

for index, row in values.iterrows():
    print(index, row)



