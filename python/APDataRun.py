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

values['ALLIANZ'] = values['ALLIANZ'] / xrate['EURUSD']

values['LLOYDS BANKING GROUP'] = values['LLOYDS BANKING GROUP'] / xrate['GBPUSD']

values['BT GROUP'] = values['BT GROUP'] / xrate['GBPUSD']

values['DEUTSCHE POST'] = values['DEUTSCHE POST'] / xrate['EURUSD']

temp = np.zeros(7)
tempSum = 0.0
shares = np.zeros(7)
index = np.zeros(nrows)
divisor = 1.0

i = 0

index[0] = values['APPLE'][i] * values['APPLE - NUMBER OF SHARES'][i] * values['APPLE - FREE FLOAT NOSH'][i] / 100 + \
    values['ALLIANZ'][i] * values['ALLIANZ - NUMBER OF SHARES'][i] * values['ALLIANZ - FREE FLOAT NOSH'][i] / 100 + \
    values['GENERAL ELECTRIC'][i] * values['GENERAL ELECTRIC - NUMBER OF SHARES'][i] * values['GENERAL ELECTRIC - FREE FLOAT NOSH'][i] / 100 + \
    values['LLOYDS BANKING GROUP'][i] * values['LLOYDS BANKING GROUP - NUMBER OF SHARES'][i] * values['LLOYDS BANKING GROUP - FREE FLOAT NOSH'][i] / 100 + \
    values['BT GROUP'][i] * values['BT GROUP - NUMBER OF SHARES'][i] * values['BT GROUP - FREE FLOAT NOSH'][i] / 100 + \
    values['DEUTSCHE POST'][i] * values['DEUTSCHE POST - NUMBER OF SHARES'][i] * values['DEUTSCHE POST - FREE FLOAT NOSH'][i] / 100 + \
    values['JOHNSON & JOHNSON'][i] * values['JOHNSON & JOHNSON - NUMBER OF SHARES'][i] * values['JOHNSON & JOHNSON - FREE FLOAT NOSH'][i] / 100

for i in range(1, nrows):
    temp[0] = values['APPLE'][i] * values['APPLE - NUMBER OF SHARES'][i] * values['APPLE - FREE FLOAT NOSH'][i] / 100
    temp[1] = values['ALLIANZ'][i] * values['ALLIANZ - NUMBER OF SHARES'][i] * values['ALLIANZ - FREE FLOAT NOSH'][i] / 100
    temp[2] = values['GENERAL ELECTRIC'][i] * values['GENERAL ELECTRIC - NUMBER OF SHARES'][i] * values['GENERAL ELECTRIC - FREE FLOAT NOSH'][i] / 100
    temp[3] = values['LLOYDS BANKING GROUP'][i] * values['LLOYDS BANKING GROUP - NUMBER OF SHARES'][i] * values['LLOYDS BANKING GROUP - FREE FLOAT NOSH'][i] / 100
    temp[4] = values['BT GROUP'][i] * values['BT GROUP - NUMBER OF SHARES'][i] * values['BT GROUP - FREE FLOAT NOSH'][i] / 100
    temp[5] = values['DEUTSCHE POST'][i] * values['DEUTSCHE POST - NUMBER OF SHARES'][i] * values['DEUTSCHE POST - FREE FLOAT NOSH'][i] / 100
    temp[6] = values['JOHNSON & JOHNSON'][i] * values['JOHNSON & JOHNSON - NUMBER OF SHARES'][i] * values['JOHNSON & JOHNSON - FREE FLOAT NOSH'][i] / 100

    tempSum = np.sum(temp)



    shares[0] = values['APPLE - NUMBER OF SHARES'][i-1] / values['APPLE - NUMBER OF SHARES'][i]
    shares[1] = values['ALLIANZ - NUMBER OF SHARES'][i-1] / values['ALLIANZ - NUMBER OF SHARES'][i]
    shares[2] = values['GENERAL ELECTRIC - NUMBER OF SHARES'][i-1] / values['GENERAL ELECTRIC - NUMBER OF SHARES'][i]
    shares[3] = values['LLOYDS BANKING GROUP - NUMBER OF SHARES'][i-1] / values['LLOYDS BANKING GROUP - NUMBER OF SHARES'][i]
    shares[4] = values['BT GROUP - NUMBER OF SHARES'][i-1] / values['BT GROUP - NUMBER OF SHARES'][i]
    shares[5] = values['DEUTSCHE POST - NUMBER OF SHARES'][i-1] / values['DEUTSCHE POST - NUMBER OF SHARES'][i]
    shares[6] = values['JOHNSON & JOHNSON - NUMBER OF SHARES'][i-1] / values['JOHNSON & JOHNSON - NUMBER OF SHARES'][i]

    divisor = (2*tempSum - np.dot(temp, shares)) / tempSum

    index[i] = tempSum / divisor

np.savetxt("index.csv", index, delimiter=",")







