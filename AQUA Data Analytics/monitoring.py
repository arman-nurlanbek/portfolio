# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification.
# 
# This module will access data from the LondonAir Application Programming Interface (API)
# The API provides access to data to monitoring stations. 
# 
# You can access the API documentation here http://api.erg.ic.ac.uk/AirQuality/help
#

  
import datetime
def get_live_data_from_api(site_code='MY1',species_code='NO',start_date=datetime.date(2022, 12, 6),end_date=None):
    """
    Return data from the LondonAir API using its AirQuality API. 
    
    *** This function is provided as an example of how to retrieve data from the API. ***
    It requires the `requests` library which needs to be installed. 
    In order to use this function you first have to install the `requests` library.
    This code is provided as-is. 
    """
    import requests
    import datetime
    import json
    start_date = datetime.date.today() if start_date is None else start_date
    end_date = start_date + datetime.timedelta(days=1) if end_date is None else end_date
    #
    
    endpoint = "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json"
   
    url = endpoint.format(
        site_code = site_code,
        species_code = species_code,
        start_date = start_date,
        end_date = end_date
    )
    
    res = requests.get(url)
    text = json.dumps(res.json(), sort_keys=False, indent=4)
    print(text)
    print(type(datetime.date.today()))
    return res.json()
  
#get_live_data_from_api()

"""Functions: """


def today_average(site_code, species_code = 'NO', start_date = None, end_date = None):
  """ The purpose of the function is to find average pollution level at specific date or number of days
  The function returns average number of pollution level
  The function uses requests module to make an API requests and datetime module to indicate specific date
  Example of input: today_average('MY1')
  Example of output: Average pollution value for 2022-11-02 is 13
  """
  
  
  import requests
  import datetime
  
  # Set start date for today if start date was not specified
  start_date = datetime.date.today() if start_date is None else start_date
  # Set end date for the end of the day if end date was not specified
  end_date = start_date + datetime.timedelta(days=1) if end_date is None else end_date
  
  # URL of API
  url = "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json"
  # Set format of url for json 
  url = url.format(
    site_code = site_code,
    species_code = species_code,
    start_date = start_date,
    end_date = end_date
  )
  # Make a request
  response = requests.get(url)
  # Assign json of a request 
  data = response.json()
  # Assign dictionaries with values from data to a list
  into_dict_list = data['RawAQData']['Data']
  
  list_of_pollution_values = []

  sum_of_pollution_values = 0
  
  # Loop takes values from dictionaries in into_dict_list by index
  for element in range(len(into_dict_list)):
    list_of_dictionary_values = list(into_dict_list[element].values())
    # Append values to the list
    list_of_pollution_values.append(list_of_dictionary_values[1])
    # Loop converts values to float and make a sum of float 
  for element in list_of_pollution_values:
    if element == '':
      sum_of_pollution_values = sum_of_pollution_values
    else:
      sum_of_pollution_values += float(element)
  # Calculates average pollution value
  average_pollution_value = sum_of_pollution_values/len(list_of_pollution_values)
  # Output
  average_pollution_value_output = 'Average pollution value for ' +str(datetime.date.today())+ ' is '   + str(average_pollution_value)
    
  print(average_pollution_value_output)  
  # Returns average pollution value
  return average_pollution_value


def air_polution_indexes_of_monitoring_sites(site_codes):
  """ The purpose of the function is to output air polution indexes of given monitoring sites
  The function returns a dictionary with air pollution indexes
  The The function uses requests module to make a API requests 
  Example of input: air_polution_indexes_of_monitoring_sites(['BX1', 'RB7', 'RI2'])
  Example of output: {1}
  """
  import requests
  
  # Dictionary with data of monitoring sites
  datas = {}
  # Loop iterate over every monitoring site in given site_codes list
  for site_code in site_codes:
    # URL of API
    url = "https://api.erg.ic.ac.uk/AirQuality//Daily/MonitoringIndex/Latest/SiteCode={site_code}/Json"
    # Set format of url for json 
    url = url.format(
      site_code = site_code
    )
    # Make a request
    response = requests.get(url)
    # Assign json of a request
    data = response.json()
    # In case of lack of air index polltuion in data - KeyError
    try:
      # Take only air quality indexes
      air_quality_index = data['DailyAirQualityIndex']['LocalAuthority']['Site']['Species'][0]
    except KeyError:
      break
    # Updates dictionary with found air qulity index corresponding to monitoring site
    datas.update({site_code: air_quality_index})
    
    print(site_code,datas[site_code])
  
  # Return dictionary 
  return datas


def compare():
  """ The purpose of the function is to compare average air quality indexes of monitoring sites
  by interacting with user
  The function returns dictionary with sorted average air quiality indexes
  The function uses requests module to make a API requests and dict() to update and sort dictionary
  Example of input: compare()
  Example of output: {RB7: 1, MY1: 3, RI2: 5, ...}
  """
  # Number of monitoring sites for comparison
  compare_number = int(input('Enter number of Monitoring Sites you want to compare: '))
  # List of monitoring sites
  sites = []
  # Loop makes a list of monitoring sites 
  for i in range(compare_number):
    # Input monitoring site
    monitoring_site = str(input("Type a monitoring site:"))
    # Makes monitoring site RB7 in case monitoring site is not given
    if monitoring_site == '':
      monitoring_site = 'RB7'
      # Check if monitoring site is given correctly
    elif len(monitoring_site) != 3:
      monitoring_site = str(input("Type a monitoring site:"))
    else:
      monitoring_site = monitoring_site
      # Append monitoring site to the list
    sites.append(monitoring_site)
    
  # List comprehension that uses today_average() function to find average quality index
  values = [today_average(value) for value in sites]
  # Dictionary of values
  dict_values = {}
  
  # Loop adds element of site and value to dict_values dictionary
  for site, value in zip(sites,values):
    dict_values.update({site:value})
  # Sorts dictionary elements by values in ASC order
  dict_values = dict(sorted(dict_values.items(), key=lambda item: item[1]))
  print(dict_values)
  # Returns the dictionary
  return dict_values
  

def total_information(site_code = None, start_date = None):
  
  """ The purpose of the function is to give total information of a monitoring site started from given date.
  The function output a json file with all information sorted.
  The function usees requests module to make an API  requests and json to work with data
  Example of input: total_information()
  Example of output: "total_information.json"
  """
  import requests
  import json
  
  # Set site_code to MY1 if site_code was not specified
  site_code = 'MY1' if site_code == None else site_code
  # Set start_date to 2021-01-01 if start_date was not specified
  start_date = '2021-01-01' if start_date == None else start_date
  # URL of API
  url = "https://api.erg.ic.ac.uk/AirQuality/Annual/MonitoringObjective/SiteCode={site_code}/StartDate={start_date}/Json"
  # Set format of url for json 
  url = url.format(
    site_code = site_code,
    start_date = start_date
  )
  # Make a request
  response = requests.get(url)
  # Assign json of a request 
  data = response.json()
  # List of keys for the dictionary 
  keys = []
  # List of values for the dictionary
  values = []
  # Loop fill keys list with name of pollution quality and values list with values of pollution quality
  for species in range(len(data['SiteObjectives']['Site']['Objective'])):
    keys.append(data['SiteObjectives']['Site']['Objective'][species]['@SpeciesDescription'])
    values.append(data['SiteObjectives']['Site']['Objective'][species]['@ObjectiveName'])
  # Dictionary with information
  information_dict = {}
  # Set dictionary keys to an empty key
  for key in keys:
    information_dict[key] = []
  # Append keys and values to information dict
  for key,value in zip(keys,values):
    information_dict[key].append(value)
    
  # Write information_dict to a file "total_information.json"
  with open("total_information.json", "w") as f:
    # write the dictionary to the file in JSON format
    json.dump(information_dict, f, indent=4, sort_keys=True)
    

  

    
  