import os
import pandas as pd

file_path = '../data/XTAL_Challange.xlsx'

xl = pd.ExcelFile(file_path)

sheetname = xl.sheet_names[2]

nrows = 1307

# currency = pd.read_excel(file_path, sheet_name=0, skiprows=1)

xrate = pd.read_excel(file_path, sheet_name=2, skiprows=0, nrows=nrows)

values = pd.read_excel(file_path, sheet_name=1, skiprows=0, nrows=nrows)

values['ALLIANZ'] = values['ALLIANZ'] / xrate['EURUSD']

values['LLOYDS BANKING GROUP'] = values['LLOYDS BANKING GROUP'] / xrate['GBPUSD']

values['BT GROUP'] = values['BT GROUP'] / xrate['GBPUSD']

values['DEUTSCHE POST'] = values['DEUTSCHE POST'] / xrate['EURUSD']

Mt = values['APPLE'] * values['APPLE - NUMBER OF SHARES'] * values['APPLE - FREE FLOAT NOSH'] / 100 + \
     values['ALLIANZ'] * values['ALLIANZ - NUMBER OF SHARES'] * values['ALLIANZ - FREE FLOAT NOSH'] / 100 + \
     values['GENERAL ELECTRIC'] * values['GENERAL ELECTRIC - NUMBER OF SHARES'] * values['GENERAL ELECTRIC - FREE FLOAT NOSH'] / 100 + \
     values['LLOYDS BANKING GROUP'] * values['LLOYDS BANKING GROUP - NUMBER OF SHARES'] * values['LLOYDS BANKING GROUP - FREE FLOAT NOSH'] / 100 + \
     values['BT GROUP'] * values['BT GROUP - NUMBER OF SHARES'] * values['BT GROUP - FREE FLOAT NOSH'] / 100 + \
     values['DEUTSCHE POST'] * values['DEUTSCHE POST - NUMBER OF SHARES'] * values['DEUTSCHE POST - FREE FLOAT NOSH'] / 100 + \
     values['JOHNSON & JOHNSON'] * values['JOHNSON & JOHNSON - NUMBER OF SHARES'] * values['JOHNSON & JOHNSON - FREE FLOAT NOSH'] / 100

print(f"Excel file: {Mt} ")
