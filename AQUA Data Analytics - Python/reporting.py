# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification
from pandas import *     
import pandas as pd   


def daily_average(monitoring_station:str,pollutant:str):
    """  The purpose of this function is to calculate average number of pollutant values of each day in a monitoring station.
    The function returns a list with 365 values corresponding to 365 days of the year.
    The function used read_csv to work with csv file. For this function I tried to implement all other functions from scratch
    without using any predefined functions.
    Example of input: daily_average("Pollution-London Marylebone Road.csv", 'pm10')
    Example of output: [23.45, 23.12, 49.21, .....]
    """
    #List of all daily average values that will return
    average_list = [] 
    # Read csv file 
    data = read_csv(monitoring_station) 
     # Converts all data under pollutant column into a list
    pm = data[pollutant].tolist()
    
    # Index of each value in list - numbers
    value = 0
    # Constanly updating list with values of each day
    numbers = []
    
    # This function takes the lists from the while loop and after calculating the average loads the elements into "average_list"
    def average_number(list):
        # Sum of values in each day       
        average = 0
        # Loop changes 'No data' to 0 for further calculations
        for number in list:
            if number == 'No data':
                number = 0
            # Add values converted from string to float from number list to average 
            average = average + float(number)
            # Appends average number to average_list rounded to 2 decimal places.
        average_list.append(round(average/24, 2))

    #This while loop divide all the values from the "pm" list to other lists by the each day
    
    # Stops while loop when numbers list has 24 values corresponding to 24 hours of each day and average_list has 365 values
    #       corresponding to 365 days of a year
    while len(numbers) <24 and len(average_list) < 365: 
        # Append values from pm list corresponding to pollutant column to numbers list from the first value
        numbers.append(pm[value])
        value = value + 1           
        #Runs average_number average_number(list) function when numbers list contains 24 values.               
        if len(numbers) ==24:
            average_number(numbers)
            numbers = []
    
    print(average_list)
    # Returns average_list
    return average_list
    
        
def daily_median(monitoring_station: str, pollutant: str):
    """ The purpose of this function is to calculate median number of pollutant values of each day in a monitoring station.
    The function returns a list with 365 values corresponding to 365 days of the year.
    The function used read_csv to work with csv file. For this function I tried to implement all other functions from scratch
    without using any predefined functions.
    Example of input: daily_median("Pollution-London Marylebone Road.csv", 'pm10') 
    Example of output: [10.3, 11.7, 4.23, .....]
    """
    # Statistics module to calculate median value 
    import statistics
    #List of all daily median values that will return
    median_final_list = [] 
    # Sum of values of each day
    median_float_list = []
     # Read csv file 
    data = read_csv(monitoring_station) 
    # Converts all data under specific columns into lists
    pm = data[pollutant].tolist()
    
    # Index of each value in list - numbers
    value = 0
    # Constanly updating list with values of each day
    numbers = []
    
    # This function takes the lists from the while loop and load the calculated median using "statistics" module
    def median_number(list):     
        # Loop changes 'No data' to 0 for further calculations
        for number in list:
            if number == 'No data':
                number = 0
            median_float_list.append(float(number))
        # Appends median number to median_final_list rounded to 2 deciaml places.
        median_final_list.append(round(statistics.median(median_float_list), 2))
    
    #This while loop divide all the values from the "pm" list to other lists by the each day
    
    # Stops while loop when numbers list has 24 values corresponding to 24 hours of each day and average_list has 365 values
    #       corresponding to 365 days of a year
    while len(numbers) <24 and len(median_final_list) < 365:  #This while loop divide all the values from the "pm" list to other lists by the each day
        # Append values from pm list corresponding to pollutant column to numbers list from the first value
        numbers.append(pm[value])
        value = value + 1                  
        #Runs average_number median_number(list) function when numbers list contains 24 values.               
        if len(numbers) ==24:
            median_number(numbers)
            numbers = []
        
    print(median_final_list)
    return median_final_list
        

def hourly_average(monitoring_station: str, pollutant: str):
    """  The purpose of this function is to calculate average number of pollutant values of each hour in a monitoring station.
    The function returns a list with 24 values corresponding to each hour days of a day.
    The function uses read_csv to work with csv file. For this function I tried to implement all other functions from scratch
    without using any predefined functions.
    Example of input: daily_average("Pollution-London Marylebone Road.csv", 'pm10')
    Example of output: [23.45, 23.12, 49.21, .....]
    """
    #List of all daily average values that will return
    average_list = [] 
    # Read csv file 
    data = read_csv(monitoring_station) 
    # Converts all data under specific columns into lists
    pm = data[pollutant].tolist()
    # Index of each value in list - numbers
    value = 0
    
    # This function takes the lists from the while loop and after calculating the average loads the elements into "average_list"
    def average_number(list):     
        # Sum of values in each day 
        average = 0
        # Loop changes 'No data' to 0 for further calculations
        for number in list:
            if number == 'No data':
                number = 0
            # Add values converted from string to float from number list to average 
            average = average + float(number)
            # Appends average number to average_list rounded to 2 decimal places.
        average_list.append(round(average/365, 2))
        
    # Constanly updating list with values of each day    
    numbers = []
    
    #This while loop divide all the values from the "pm" list to other lists by the hours
    
    # Stops while loop when numbers list has 365 values corresponding to each hour of all days and average_list has 24 values
    #       corresponding to 24 houes of a day
    while len(numbers) < 365 and len(average_list) < 24:
        # Append values from pm list corresponding to pollutant column to numbers list from the first value
        numbers.append(pm[value])
        value = value + 24  
        #Runs average_number average_number(list) function when numbers list contains 365 values.          
        if len(numbers) == 365 :                
            average_number(numbers)
            value = len(average_list)
            numbers = []
            
    print(average_list)
     # Returns average_list
    return average_list

    
  
def monthly_average(monitoring_station, pollutant):
    
    data = pd.read_csv(monitoring_station)
    data['date'] = pd.to_datetime(data["date"], format="%Y-%m-%d")
    data = data.set_index('date')
    monthly_averages = data.resample('M')
    
    

def peak_hour_date(date:str, monitoring_station,pollutant):
    """ The purpose of this function is to find an hour with the highers pollutant value in given date.
    The function returns a highest pollutant value.
    The function uses pandas module to read and work with values in csv.
    It uses predefined functions: pd.to_numeric(), max(), pd.read_csv()
    Example of input: peak_hour_date('2021-01-02', Pollution-London Marylebone Road.csv", 'pm10')
    Example of output: 10.2
    """
    # Read csv using pandas
    data = pd.read_csv(monitoring_station) 
    # Take out specific date from date column
    data_with_date = data[(data.date == date)]
    # Take out pollutant values of specific date and converts them to float
    data_with_date[pollutant] = pd.to_numeric(data_with_date[pollutant], downcast = 'float')
    # Assign list table_values with pollutant values of specific date
    table_values = data_with_date[pollutant]
    # Finds highest value of table_values list
    max_value = table_values.max()
    
    print(max_value)
    # Return maximum value
    return max_value
    
    
def count_missing_data(monitoring_station,pollutant):
    """ The purpose of the function is to count how many times 'No Data' or missing data appears
    in the monitoring station
    The function returns a number of 'No data' values
    The function uses pandas to read csv file.
    Example of input: count_missing_data("Pollution-London Marylebone Road.csv", 'pm25')
    Example of output: 129
    """
    
    # Read csv file using pandas
    data = pd.read_csv(monitoring_station)
    # A list with 'No data' values under pollutant column
    data_with_NoData = data[(data[pollutant] == 'No data')]
    print("The number of ’No data’ entries are there in the data: " + str(len(data_with_NoData)))
    # Returns number of 'No Data' values
    return len(data_with_NoData)



def fill_missing_data(new_value,  monitoring_station):
    """ The purpose of the function is fill 'No data' values in csv file with any other value.
    The function uses pandas to read csv file. Also, it uses replace() predefined function
    to replace 'No data' values.
    Example of input: fill_missing_data(10, "Pollution-London Marylebone Road.csv", 'pm25')
    """
    
    # Read csv file using pandas
    data = pd.read_csv(monitoring_station)
    # Replace all 'No data' values with new_value
    data_with_new_value = data.replace('No data', new_value)
    
   
