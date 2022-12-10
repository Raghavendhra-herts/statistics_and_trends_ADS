# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 20:34:26 2022

@author: Raghavendhra Rao Devineni
"""

# Importing the libraries required
import pandas as pd
import matplotlib.pyplot as plt


def prepare_co2_data():
    '''
    In this function I'm preparing to read the dataset in a .csv format taken 
    from the Worldbank
    and returning the dataset 
    
    This is the first dataset i.e CO2 emission(metric ton per_capita)
    '''
    # reading the csv dataset through pd.read_csv
    read_data_co2 = pd.read_csv("CO2 emission(metric ton per_capita).csv")
    #Dropping the coulmns from dataset which is unnecessary
    read_data_co2 = read_data_co2.drop(columns=['Series Name','Series Code','Country Code'])
    #print("\n", read_data_co2.columns)
    # returning the variable
    return read_data_co2


def prepare_electric_data():
    '''
    In this function I'm preparing to read the dataset in a .csv format taken 
    from the Worldbank
    and returning the dataset 
    
    This is second dataset i.e electric_power_consumption(per capita)

    '''
    
    # reading the csv dataset through pd.read_csv
    read_data_electric = pd.read_csv("electric_power_consumption(per capita).csv")
    #print(read_data_electric)
    #Dropping the coulmns from dataset which is unnecessary
    read_data_electric = read_data_electric.drop(columns=['Series Name','Series Code','Country Code',])
   # print("\n", read_data_electric.columns)
    
   # returning the variable
    return read_data_electric


def fill_null_values(read_data_electric):
    '''
    In this function Im passing the attribute read_data_electric to get the data
    
    -This fuction is used to fill '0' when null values found in coulmns,
    -Here particularly I have chosen the columns: 2015 [YR2015] where entire
    found to be null

    '''
    
    # converting the particular column to numeric from object datatype through pd.to_numeric()
    read_data_electric['2015 [YR2015]'] = pd.to_numeric(read_data_electric['2015 [YR2015]'], errors='coerce')
    # find and fill '0' where ever you find NaN value
    read_data_electric['2015 [YR2015]'] = read_data_electric['2015 [YR2015]'].fillna(0)
    #print(read_data_electric['2015 [YR2015]'])


def change_the_columns(data):
    '''
    
    In this function I'm passing data attribute, which contains the dataset.
    Im renaming the column as easy understanding to read & write

    '''
    
    # Re-naming the coulmns 
    data.columns = ['Country Name', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008',
                  '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    # returning the data variable
    return data


def transpose_data(get_t_data):
    '''
    
    In this function I'm passing the attriburte get_t_data, it will send the data
    to this function for transposing the dataset.
    and return the new dataframe

    '''
    # transpose the data set
    df_t = pd.DataFrame.transpose(get_t_data)
    # getting the 0th position values to get-into list
    new_header = df_t.iloc[0].values.tolist()
    # reassign them into columns
    df_t.columns = new_header
    # get the data after from the 1: position
    df_t = df_t.iloc[1:]
    # return the variable
    return df_t


def plot_line_graph(data, title, y_label):
    '''
    
    In this function I'm passing  data attribute to represent the line graph
    Im using this function to display the line graph for five different countries

    '''
    # convert the five columns data type from object to numeric by pd.to_numeric()
    data['United Kingdom'] = pd.to_numeric(data['United Kingdom'])
    data['Russian Federation'] = pd.to_numeric(data['Russian Federation'])
    data['Japan'] = pd.to_numeric(data['Japan'])
    data['India'] = pd.to_numeric(data['India'])
    data['France'] = pd.to_numeric(data['France'])
    
    # convert index into numeric by pd.to_numeric
    df_t_index = pd.to_numeric(data.index)
    
    # line plot for CO2 emission dataset for selected 5 countries from(2000-2015)
    # using grid() for configuring the grid lines
    plt.grid()
    
    # calling the plot() and sending the required columns to produce line graph
    plt.plot(df_t_index, data['United Kingdom'], label = 'UK')
    plt.plot(df_t_index, data['Russian Federation'], label = 'Russian')
    plt.plot(df_t_index, data['Japan'], label = 'Japan')
    plt.plot(df_t_index, data['India'], label = 'India')
    plt.plot(df_t_index, data['France'], label = 'France')
    # using legend() to display the labels for representation
    plt.legend()
    plt.title(title)
    # display the title on x-axis through .xlabel()
    plt.xlabel("Years")
    # display the title on y-axis through .ylabel()
    plt.ylabel(y_label)
    # telling the matplot to show() the plot we are calling
    plt.show()


def plot_bar_graph(data, title, y_label):
    '''
    
    In this function I'm passing  data attribute to represent the bar graph
    Im using this function to display the bar graph for five different countries

    '''
    # convert the five columns data type from object to numeric by pd.to_numeric()
    data['United Kingdom'] = pd.to_numeric(data['United Kingdom'])
    data['Russian Federation'] = pd.to_numeric(data['Russian Federation'])
    data['Japan'] = pd.to_numeric(data['Japan'])
    data['India'] = pd.to_numeric(data['India'])
    data['France'] = pd.to_numeric(data['France'])
    
    # convert index into numeric by pd.to_numeric
    df_t_index = pd.to_numeric(data.index)
    
    # calling the bar graph by sending the values to display in the graph 
    data.plot( y = ['United Kingdom', 'Russian Federation','Japan', 'India', 'France'], kind = 'bar', figsize = (10,5))
    plt.title(title)
    # display the title on x-axis through .xlabel()
    plt.xlabel("Year")
    # display the title on y-axis through .ylabel()
    plt.ylabel(y_label)
    # telling the matplot to show() the plot we are calling
    plt.show()
    



if __name__ == "__main__":
    
    # calling prepare_co2_data function to return the dataset 
    # I can prepare and call this functionn for new dataset
    co2_data = prepare_co2_data()
    
    # calling electric_emission_data function to return the dataset
    # I can prepare and call this functionn for new dataset
    electric_emission_data = prepare_electric_data()
    
    # fill the null values for selected column through fill_null_values( by passing the dataset)
    fill_null_values(electric_emission_data)
    
    # rename the columns in first dataset
    co2_data = change_the_columns(co2_data)
    # rename the columns in second dataset
    electric_emission_data = change_the_columns(electric_emission_data)
    
    # transposing the data for first dataset i.e CO2-Emission
    # I can call this transpose at any time in the code and also can pass new parameter to transpose the data
    co2_data_t = transpose_data(co2_data)
    # transposing the data for second dataset i.e Electric_Power_Consumption
    electric_data_t = transpose_data(electric_emission_data)
    #print(electric_data_t)

    
    # creating and calling title for line graph
    title = "CO2 Emissions produced by countries"
    # creating and calling x-label for line graph
    y_label = "Amount of CO2 Emission released"
    # calling function to plot line-graph for CO2-emission dataset
    plot_line_graph(co2_data_t, title, y_label)
    
    # creating and calling title for line graph
    title = "Electric Power Consumption used by countries"
    # creating and calling x-label for line graph
    y_label = "Amount of Electric Power used "
    # calling the function to plot line-graph for Electric_power_consumption dataset
    plot_line_graph(electric_data_t, title, y_label)
    
    # creating and calling title for bar graph
    title = "CO2 Emissions produced by countries"
    # creating and calling x-label for bar graph
    y_label = "Amount of CO2 Emission released"
    # calling the function to plot_bar_graph for Co2_emission dataset for selected columns
    plot_bar_graph(co2_data_t, title, y_label)
    
    # creating and calling title for bar graph
    title = "Electric Power Consumption used by countries"
    # creating and calling x-label for bar graph
    y_label = "Amount of Electric Power used"
    # calling the function to plot_bar_graph for Electric_Power_Consumption dataset for selected columns
    plot_bar_graph(electric_data_t, title, y_label)
    