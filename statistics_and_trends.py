# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 20:34:26 2022

@author: Raghavendhra Rao Devineni
"""

import pandas as pd
import matplotlib.pyplot as plt


def prepare_co2_data():
    read_data_co2 = pd.read_csv("CO2 emission(metric ton per_capita).csv")
    read_data_co2 = read_data_co2.drop(columns=['Series Name','Series Code','Country Code'])
    #print("\n", read_data_co2.columns)
    return read_data_co2



def prepare_electric_data():
    read_data_electric = pd.read_csv("electric_power_consumption(per capita).csv")
    print(read_data_electric)
    read_data_electric = read_data_electric.drop(columns=['Series Name','Series Code','Country Code',])
    print("\n", read_data_electric.columns)
    
    print(read_data_electric)
    return read_data_electric


def fill_null_values(read_data_electric):
    read_data_electric['2015 [YR2015]'] = pd.to_numeric(read_data_electric['2015 [YR2015]'], errors='coerce')
    read_data_electric['2015 [YR2015]'] = read_data_electric['2015 [YR2015]'].fillna(0)
    print(read_data_electric['2015 [YR2015]'])


def change_the_columns(data):
    data.columns = ['Country Name', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008',
                  '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    return data



def transpose_data(get_t_data):
# transpose the data set
    df_t = pd.DataFrame.transpose(get_t_data)
    new_header = df_t.iloc[0].values.tolist()
    df_t.columns = new_header
    df_t = df_t.iloc[1:]
    return df_t


def plot_line_graph(data):
    # convert data type from object to numeric by pd.to_numeric()
    data['United Kingdom'] = pd.to_numeric(data['United Kingdom'])
    data['Russian Federation'] = pd.to_numeric(data['Russian Federation'])
    data['Japan'] = pd.to_numeric(data['Japan'])
    data['India'] = pd.to_numeric(data['India'])
    data['France'] = pd.to_numeric(data['France'])
    
    # convert index into numeric by pd.to_numeric
    df_t_index = pd.to_numeric(data.index)
    #print("\n", df_t_index)
    
    # line plot for CO2 emission dataset for select 5 countries(2000-2015)
    plt.plot(df_t_index, data['United Kingdom'], label = 'UK')
    plt.plot(df_t_index, data['Russian Federation'], label = 'Russian')
    plt.plot(df_t_index, data['Japan'], label = 'Japan')
    plt.plot(df_t_index, data['India'], label = 'India')
    plt.plot(df_t_index, data['France'], label = 'France')
    plt.legend()
    plt.xlabel("Years")
    plt.ylabel("Countries")
    plt.show()


def plot_bar_graph(data):
    # convert data type from object to numeric by pd.to_numeric()
    data['United Kingdom'] = pd.to_numeric(data['United Kingdom'])
    data['Russian Federation'] = pd.to_numeric(data['Russian Federation'])
    data['Japan'] = pd.to_numeric(data['Japan'])
    data['India'] = pd.to_numeric(data['India'])
    data['France'] = pd.to_numeric(data['France'])
    
    # convert index into numeric by pd.to_numeric
    df_t_index = pd.to_numeric(data.index)
    
    data.plot( y = ['United Kingdom', 'Russian Federation','Japan', 'India', 'France'], kind = 'bar', figsize = (10,5))
    plt.xlabel("Year")
    plt.ylabel("Countries")
    plt.show()
    


if __name__ == "__main__":
    
    # co2_emission dataset
    co2_data = prepare_co2_data()
    
    # electric_power_consumption dataset
    electric_emission_data = prepare_electric_data()
    
    # fill the null values for selected column
    fill_null_values(electric_emission_data)
    
    # rename the columns
    co2_data = change_the_columns(co2_data)
    electric_emission_data = change_the_columns(electric_emission_data)
    
    # transposing the data-set
    co2_data_t = transpose_data(co2_data)
    electric_data_t = transpose_data(electric_emission_data)
    
    # calling function to plot line-graph for CO2-emission dataset
    plot_line_graph(co2_data_t)
    
    # calling the function to plot line-graph for Electric_power_consumption dataset
    plot_line_graph(electric_data_t)
    
    # calling the function to plot_bar_graph for Co2_emission dataset for selected columns
    plot_bar_graph(co2_data_t)
    
    plot_bar_graph(electric_data_t)