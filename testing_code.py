# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 20:34:26 2022

@author: Raghavendhra Rao Devineni
"""

import pandas as pd
import matplotlib.pyplot as plt

read_data = pd.read_csv("CO2 emission(metric ton per_capita).csv")
# CO2 emission(metric ton per_capita)    electric_power_consumption(per capita)
#print(read_data)
#print("\n", read_data.columns)
read_data = read_data.drop(columns=['Series Name','Series Code','Country Code',])
print("\n", read_data.columns)


read_data.columns = ['Country Name', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008',
              '2009', '2010', '2011', '2012', '2013', '2014', '2015']

# print("\n \n",read_data['Series Name'].unique())

# remove all NaNs contain in rows..!
read_data = read_data.dropna(axis = 0).reset_index(drop=True)
#print(read_data)

# transpose the data set
df_t = pd.DataFrame.transpose(read_data)
print(df_t)

# removing un-necessary columns in data set
new_header = df_t.iloc[0].values.tolist()
df_t.columns = new_header
print(df_t.columns)

# removing unwanted text in first line "Country Name row"
df_t = df_t.iloc[1:]
print("\n \n",df_t)

# check and remove the if null values for columns neeed
df_t = df_t[df_t['United Kingdom'].notna()]
df_t = df_t[df_t['Russian Federation'].notna()]
df_t = df_t[df_t['Japan'].notna()]
df_t = df_t[df_t['India'].notna()]
df_t = df_t[df_t['France'].notna()]

# convert data type from object to numeric by pd.numeric
df_t['United Kingdom'] = pd.to_numeric(df_t['United Kingdom'])
df_t['Russian Federation'] = pd.to_numeric(df_t['Russian Federation'])
df_t['Japan'] = pd.to_numeric(df_t['Japan'])
df_t['India'] = pd.to_numeric(df_t['India'])
df_t['France'] = pd.to_numeric(df_t['France'])

# convert index into numeric by pd.to_numeric
df_t_index = pd.to_numeric(df_t.index)
#print("\n", df_t_index)

plt.plot(df_t_index, df_t['United Kingdom'], label = 'UK')
plt.plot(df_t_index, df_t['Russian Federation'], label = 'Russian')
plt.plot(df_t_index, df_t['Japan'], label = 'Japan')
plt.plot(df_t_index, df_t['India'], label = 'India')
plt.plot(df_t_index, df_t['France'], label = 'France')
plt.legend()
plt.xlabel("Years")
plt.ylabel("Countries")
plt.show()


#df_t['United Kingdom'].plot.bar(df_t_index)
#df_t.plot.bar(df_t_index, ['United Kingdom', 'Japan'])
df_t.plot( y = ['United Kingdom', 'Russian Federation','Japan', 'India', 'France'], kind = 'bar', figsize = (15,5))
plt.xlabel("Year")
plt.ylabel("Countries")
plt.show()