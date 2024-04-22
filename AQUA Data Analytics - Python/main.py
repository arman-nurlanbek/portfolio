# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification
from reporting import daily_average, daily_median, hourly_average, monthly_average, peak_hour_date, count_missing_data, fill_missing_data
from intelligence import find_cyan_pixels, find_red_pixels, detect_connected_components, detect_connected_components_sorted
def main_menu():
    """ The purpose of the function is to help a user navigate through functions in reporting and intelligence modules.
    A user should choose between lists of functions available and type a specific letter or combination of letters
    to run a function.
    
    Number of functions available: daily_average, daily_median, hourly_average, monthly_average, peak_hour_date, 
    count_missing_data, fill_missing_data, find_cyan_pixels, find_red_pixels, detect_connected_components, 
    detect_connected_components_sorted.
    
    For some functions user should type input of the functions, for example: monitoring_station or new_value
    """
    # Choose between different options
    choose_options = input("""
                               Welcome to ACQUA system!
                               Choose between different options:
                               R - Reporting menu
                               I - Intelligence menu
                               A - About
                               Q - Quit
                               """)
    # Run reporting_menu() 
    if choose_options == 'R' or choose_options == 'r':
        reporting_menu()
        main_menu()
    # Run intelligence_menu()
    elif choose_options == 'I' or choose_options == 'i':
        intelligence_menu()
        main_menu()
    # Run about()
    elif choose_options == 'A' or choose_options == 'a':
        about()
        main_menu()
    # Run quit()
    elif choose_options == 'Q':
        quit()
        
            

def reporting_menu():
    """ The purpose of the function is to help user navigate between functions in Reporting Module (RM)
    A user should choose between lists of functions available and type a specific letter or combination of letters
    to run a function.
    For some functions user should type input of the functions, for example: monitoring_station or new_value.
    """
    # Choose between options
    choose_options = input("""
                           Reporting Menu
                           Choose between different options:
                           A - Daily average
                           M - Daily Median
                           H - Hourly Average
                           MA - Monthly Average
                           P - Peak Hour Date
                           C - Count Missing Data
                           F - Fill Missing Data
                           B - Go back to main menu
                           Q - Quit
                           """)
    # Run if a user chooses 'A' or 'M' or 'H' or 'MA' or 'P' or 'C', as this functions ask for identitacal parameters
    if choose_options == 'A' or 'M' or 'H' or 'MA' or 'P' or 'C':
        # Ask a user for choosing monitoring station
        choose_monitoring_station = input("""Choose Monitoring Station:
                                          K - London N Kensington
                                          M - London Marylebone Road
                                          H - London Harlington
                                          B - Back
                                          """)
        # Run if chooses London N Kensigton
        if choose_monitoring_station == "K" and choose_options == 'A' or 'M' or 'H' or 'MA' or 'P' or 'C':
            # Assign the variable to London N Kensigton
            monitoring_station = 'Pollution-London N Kensington.csv'
        # Run if chooses London Marylebone Road
        elif choose_monitoring_station == 'M' and choose_options == 'A' or 'M' or 'H' or 'MA' or 'P' or 'C':
            # Assign the variable to London Marylebone Road
            monitoring_station = 'Pollution-London Marylebone Road.csv'
        # Run if chooses London Harlingtion
        elif choose_monitoring_station == 'H' and choose_options == 'A' or 'M' or 'H' or 'MA' or 'P' or 'C':
            # Assign the variable to London Harlingtion
            monitoring_station = 'Pollution-London Harlington.csv'
        # Run if chooses 'B', goes back to Main Menu
        elif choose_monitoring_station == 'B':
            main_menu()
        # Run if chooses 'F' and London N Kensigton
        elif choose_options == 'F' and choose_monitoring_station == 'K':
           # Assign the variable to London N Kensigton
           monitoring_station = 'Pollution-London N Kensington.csv'
           # Ask for New value parameter
           new_value = input('Choose new value: ')
           fill_missing_data(new_value, monitoring_station)
           # Goes back to Main Menu
           main_menu()
        
        
        # Choose pollutant    
        choose_pollutant = input("""Choose Pollutant:
                                 10 - pm10
                                 25 = pm25
                                 """)
        # Run if pollutant = 10 and option = A
        if choose_pollutant == '10' and choose_options == 'A':
            pollutant = 'pm10'
            # Finally executes chosen funtion
            daily_average(monitoring_station, pollutant)
            reporting_menu()
        # Run if pollutant = 25 and option = A
        elif choose_pollutant == '25' and choose_options == 'A':
            pollutant = 'pm25'
            # Finally executes chosen funtion
            daily_average(monitoring_station, pollutant)
            reporting_menu()
        # Run if pollutant = 10 and option = M
        elif choose_pollutant == '10' and choose_options == 'M':
            pollutant = 'pm10'
            # Finally executes chosen funtion
            daily_median(monitoring_station, pollutant)
            reporting_menu()
        # Run if pollutant = 25 and option = M
        elif choose_pollutant == '25' and choose_options == 'M':
            pollutant = 'pm25'
            # Finally executes chosen funtion
            daily_median(monitoring_station, pollutant)
            reporting_menu()
        # Run if pollutant = 10 and option = H
        elif choose_pollutant == '10' and choose_options == 'H':
            pollutant = 'pm10'
            # Finally executes chosen funtion
            hourly_average(monitoring_station, pollutant)
            reporting_menu()
        # Run if pollutant = 25 and option = H
        elif choose_pollutant == '25' and choose_options == 'H':
            pollutant = 'pm25'
            # Finally executes chosen funtion
            hourly_average(monitoring_station, pollutant)
            reporting_menu()
        # Run if pollutant = 10 and option = MA
        elif choose_pollutant == '10' and choose_options == 'MA':
            pollutant = 'pm10'
            monthly_average(monitoring_station, pollutant)
            reporting_menu()
        # Run if pollutant = 25 and option = MA
        elif choose_pollutant == '25' and choose_options == 'MA':
            pollutant = 'pm25'
            # Finally executes chosen funtion
            monthly_average(monitoring_station, pollutant)
            reporting_menu()
        # Run if pollutant = 10 and option = P
        elif choose_pollutant == '10' and choose_options == 'P':
            pollutant = 'pm10'
            # Finally executes chosen funtion
            peak_hour_date(monitoring_station, pollutant)
            reporting_menu()
        # Run if pollutant = 25 and option = P
        elif choose_pollutant == '25' and choose_options == 'P':
            pollutant = 'pm25'
            # Finally executes chosen funtion
            peak_hour_date(monitoring_station, pollutant)
            reporting_menu()
        # Run if pollutant = 10 and option = C
        elif choose_pollutant == '10' and choose_options == 'C':
            pollutant = 'pm10'
            # Finally executes chosen funtion
            count_missing_data(monitoring_station, pollutant)
            reporting_menu()
        # Run if pollutant = 25 and option = C
        elif choose_pollutant == '25' and choose_options == 'C':
            pollutant = 'pm25'
            # Finally executes chosen funtion
            count_missing_data(monitoring_station, pollutant)
            reporting_menu()

        
    
        
        
    
    
    


def intelligence_menu():
    """ The purpose of the function is to help user navigate between functions in Intelligence Module (RM)
    A user should choose between lists of functions available and type a specific letter or combination of letters
    to run a function.
    For some functions user should type input of the functions, for example: map.png
    """
    # Choose between options
    choose_options = input("""Choose options:
                           R - Find red pixels
                           C - Find cyan pixels
                           CC - Find connected components
                           CCS - Find connected components sorted
                           """)
    # Run if a user chooses R
    if choose_options == 'R':
        # Ask for a filename
        map_filename = input("Choose file name: ")
        find_red_pixels(map_filename)
    # Run if a user chooses C
    elif choose_options == 'C':
        # Ask for a filename
        map_filename = input("Choose file name: ")
        find_cyan_pixels(map_filename)
    # Run if a user chooses CC
    elif choose_options == 'CC':
        # Ask for a filename
        map_filename = input("Choose file name: ")
        detect_connected_components(map_filename)
    # Run if user chooses CCS
    elif choose_options == 'CCS':
        # Ask for a filename
        map_filename = input("Choose file name: ")
        detect_connected_components_sorted(map_filename)
        
        
def about():
    "The function prints the module's number and candidate number"
    module = 'ECM 1400'
    candidate_number = '242598'
    print(module)
    print(candidate_number)
    return module, candidate_number

def quit():
    "The function quit from the main menu and stops the function"
    while True:
        break
        




if __name__ == '__main__':
    main_menu()