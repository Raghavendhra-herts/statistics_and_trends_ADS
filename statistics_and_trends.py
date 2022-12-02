# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 10:26:15 2022

@author: Raghavendhra Rao Devineni
"""

import pandas as pd
import matplotlib.pyplot as plt

read_data = pd.read_csv("GDP(current US$)1.csv")
#print(read_data)
#print("\n", read_data.columns)
read_data = read_data.drop(columns=['Series Code','Country Code',])
print("\n", read_data.columns)


read_data.columns = ['Series Name','Country Name', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008',
              '2009', '2010', '2011', '2012', '2013', '2014', '2015']

print("\n \n",read_data['Series Name'].unique())




#print("\n \n","remove all NaNs contain in rows..!")
read_data = read_data.dropna(axis = 0).reset_index(drop=True)
#print(read_data)

#print("\n", "transpose the data set")
df_t = pd.DataFrame.transpose(read_data)
print(df_t)

#print("\n","removing un-necessary columns in data set")

new_header = df_t.iloc[0].values.tolist()
df_t.columns = new_header
print(df_t.columns)


# removing unwanted text in first line "Country Name row"
df_t = df_t.iloc[1:]
print("\n \n",df_t)


#print("\n", df_t.iloc[:,1:5])


'''
df_t['India'] = df_t['India'].apply(pd.to_numeric, errors='coerce')
print(df_t['India'])
df_t['Algeria'] = df_t['Algeria'].apply(pd.to_numeric, errors='coerce')
##df_t['New Zealand'] = df_t['New Zealand'].apply(pd.to_numeric, errors='coerce')
df_t['Argentina'] = df_t['Argentina'].apply(pd.to_numeric, errors='coerce')
df_t['China'] = df_t['China'].apply(pd.to_numeric, errors='coerce')
df_t['Japan'] = df_t['Japan'].apply(pd.to_numeric, errors='coerce')
df_t['Denmark'] = df_t['Denmark'].apply(pd.to_numeric, errors='coerce')
print("\n", df_t.dtypes)
data = df_t.iloc[:,0:220]
print(data.columns)
df_t_index = pd.to_numeric(data.index)
print(df_t_index)
plt.plot(df_t_index, data['Algeria'], label = 'Algeria')
plt.plot(df_t_index, data['India'], label = 'India')
#plt.plot(df_t_index, data['New Zealand'], label = 'New Zealand')# 
plt.plot(df_t_index, data['Argentina'], label = 'Argentina')
plt.plot(df_t_index, data['China'], label = 'China')
plt.plot(df_t_index, data['Japan'], label = 'Japan')# 
plt.plot(df_t_index, data['Denmark'], label = 'Denmark')
plt.legend()
#plt.show()

'''

