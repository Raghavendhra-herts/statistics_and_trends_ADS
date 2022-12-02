# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 20:34:26 2022

@author: Raghavendhra Rao Devineni
"""

import pandas as pd
import matplotlib.pyplot as plt

read_data_co2 = pd.read_csv("CO2 emission(metric ton per_capita).csv")
# CO2 emission(metric ton per_capita)    electric_power_consumption(per capita)
#print(read_data)
#print("\n", read_data.columns)
read_data_co2 = read_data_co2.drop(columns=['Series Name','Series Code','Country Code',])
#print("\n", read_data_co2.columns)



read_data_electric = pd.read_csv("electric_power_consumption(per capita).csv")
print(read_data_electric)
read_data_electric = read_data_electric.drop(columns=['Series Name','Series Code','Country Code',])
print("\n", read_data_electric.columns)


read_data_electric['2015 [YR2015]'] = pd.to_numeric(read_data_electric['2015 [YR2015]'],errors='coerce')
read_data_electric['2015 [YR2015]'] = read_data_electric['2015 [YR2015]'].fillna(0)
print(read_data_electric['2015 [YR2015]'])



read_data_co2.columns = ['Country Name', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008',
              '2009', '2010', '2011', '2012', '2013', '2014', '2015']
read_data_electric.columns = ['Country Name', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008',
              '2009', '2010', '2011', '2012', '2013', '2014', '2015']
print(read_data_electric)

# print("\n \n",read_data['Series Name'].unique())




'''
# remove all NaNs contain in rows..!
read_data_co2 = read_data_co2.dropna(axis = 0).reset_index(drop=True)
#print(read_data)
read_data_electric = read_data_electric.dropna(axis = 0).reset_index(drop=True)
print(read_data_electric)
'''



# transpose the data set
df_t_co2 = pd.DataFrame.transpose(read_data_co2)
df_t_electric = pd.DataFrame.transpose(read_data_electric)
print(df_t_electric)



# removing un-necessary columns in data set
new_header = df_t_co2.iloc[0].values.tolist()
df_t_co2.columns = new_header
#print(df_t.columns)

# electric_emission
new_header = df_t_electric.iloc[0].values.tolist()
df_t_electric.columns = new_header
print(df_t_electric)



# removing unwanted text in first line "Country Name row"
df_t_co2 = df_t_co2.iloc[1:]
#print("\n \n",df_t)
df_t_electric = df_t_electric.iloc[1:]
print("\n \n",df_t_electric)



# check and remove the if null values for columns neeed in CO2-emission dataset
df_t_co2 = df_t_co2[df_t_co2['United Kingdom'].notna()]
df_t_co2 = df_t_co2[df_t_co2['Russian Federation'].notna()]
df_t_co2 = df_t_co2[df_t_co2['Japan'].notna()]
df_t_co2 = df_t_co2[df_t_co2['India'].notna()]
df_t_co2 = df_t_co2[df_t_co2['France'].notna()]




# convert data type from object to numeric by pd.to_numeric()
df_t_co2['United Kingdom'] = pd.to_numeric(df_t_co2['United Kingdom'])
df_t_co2['Russian Federation'] = pd.to_numeric(df_t_co2['Russian Federation'])
df_t_co2['Japan'] = pd.to_numeric(df_t_co2['Japan'])
df_t_co2['India'] = pd.to_numeric(df_t_co2['India'])
df_t_co2['France'] = pd.to_numeric(df_t_co2['France'])


#convert the below datatype to numeric through pd.to_numeric()
df_t_electric['United Kingdom'] = pd.to_numeric(df_t_electric['United Kingdom'])
df_t_electric['Russian Federation'] = pd.to_numeric(df_t_electric['Russian Federation'])
df_t_electric['Japan'] = pd.to_numeric(df_t_electric['Japan'])
df_t_electric['India'] = pd.to_numeric(df_t_electric['India'])
df_t_electric['France'] = pd.to_numeric(df_t_electric['France'])




# convert index into numeric by pd.to_numeric
df_t_index = pd.to_numeric(df_t_co2.index)
#print("\n", df_t_index)

#convert index into numeric through pd.to_numeric()
df_t_index_electric = pd.to_numeric(df_t_electric.index)
print("\n ", df_t_electric)


# line plot for CO2 emission dataset for select 5 countries(2000-2015)
plt.plot(df_t_index, df_t_co2['United Kingdom'], label = 'UK')
plt.plot(df_t_index, df_t_co2['Russian Federation'], label = 'Russian')
plt.plot(df_t_index, df_t_co2['Japan'], label = 'Japan')
plt.plot(df_t_index, df_t_co2['India'], label = 'India')
plt.plot(df_t_index, df_t_co2['France'], label = 'France')
plt.legend()
plt.xlabel("Years")
plt.ylabel("Countries")
plt.show()

# line plot for electric power consumption for selected 5 countries(2000-2015)
plt.plot(df_t_index_electric, df_t_electric['United Kingdom'], label = 'UK')
plt.plot(df_t_index_electric, df_t_electric['Russian Federation'], label = 'Russian')
plt.plot(df_t_index_electric, df_t_electric['Japan'], label = 'Japan')
plt.plot(df_t_index_electric, df_t_electric['India'], label = 'India')
plt.plot(df_t_index_electric, df_t_electric['France'], label = 'France')
plt.legend()
plt.xlabel("Years")
plt.ylabel("Countries")
plt.show()


#df_t['United Kingdom'].plot.bar(df_t_index)
#df_t.plot.bar(df_t_index, ['United Kingdom', 'Japan'])
df_t_co2.plot( y = ['United Kingdom', 'Russian Federation','Japan', 'India', 'France'], kind = 'bar', figsize = (10,5))
plt.xlabel("Year")
plt.ylabel("Countries")
plt.show()


#bar grapth representing countries from 2000 to 2015
df_t_electric.plot(y = ['United Kingdom', 'Russian Federation','Japan', 'India', 'France'], kind = 'bar', figsize = (10,5))
plt.show()