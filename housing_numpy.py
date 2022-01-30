import os
import csv
import numpy as np

filepath = os.getcwd() + "/housing.csv"

df = np.loadtxt(filepath, delimiter=',', skiprows=1, usecols=(8,9), dtype={'names': ('median_house_value', 'ocean_proximity'), 'formats': ('f', 'S10')})

hour_ocean = 0.
num_hour_ocean = 0
near_ocean = 0.
num_near_ocean = 0
near_bay = 0.
num_near_bay = 0
inland = 0.
num_inland = 0
island = 0.
num_island = 0

for i in range(len(df)):
    if (df[i]['ocean_proximity'] == b'NEAR BAY'):
        near_bay += df[i]['median_house_value']
        num_near_bay += 1
    elif (df[i]['ocean_proximity'] == b'<1H OCEAN'):
        hour_ocean += df[i]['median_house_value']
        num_hour_ocean += 1
    elif (df[i]['ocean_proximity'] == b'NEAR OCEAN'):
        near_ocean += df[i]['median_house_value']
        num_near_ocean += 1
    elif (df[i]['ocean_proximity'] == b'INLAND'):
        inland += df[i]['median_house_value']
        num_inland += 1
    elif (df[i]['ocean_proximity'] == b'ISLAND'):
        island += df[i]['median_house_value']
        num_island += 1

hour_ocean /= num_hour_ocean
near_ocean /= num_near_ocean
near_bay /= num_near_bay
inland /= num_inland
island /= num_island

df2 = np.array([('ISLAND', island), ('INALND', inland), ('NEAR OCEAN', near_ocean), ('NEAR_BAY', near_bay), ('<1H OCEAN', hour_ocean)], dtype={'names': ('ocean_proximity', 'average_median_house_value'), 'formats': ('S10', 'f')})

temp = 0.
temp2 = ' '
for i in range(len(df2)):
    j = i
    for j in range(len(df2) - 1):
        if (df2[j]['average_median_house_value'] < df2[j + 1]['average_median_house_value']):
            temp = df2[j + 1]['average_median_house_value']
            temp2 = df2[j + 1]['ocean_proximity']
            df2[j + 1]['average_median_house_value'] = df2[j]['average_median_house_value']
            df2[j + 1]['ocean_proximity'] = df2[j]['ocean_proximity']
            df2[j]['average_median_house_value'] = temp
            df2[j]['ocean_proximity'] = temp2
print(df2)

np.savetxt('housing_numpy.csv', df2, delimiter=',')