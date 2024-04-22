# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification


def sumvalues(values):
  """ The purpose of the function is to make sum of values in a given list
  The function returns sum of values
  The function does not use any predefined functions
  Example of input: [1,2,3,4]
  Example of output: 10
  """
  # Sum variable
  sum = 0
  # Loop raises ValueError if not int or float was given in the list  
  for value in values:
      if not isinstance(value, (int, float)):
          raise ValueError('Non-numerical value present in the list') 
      # Add value to sum 
      sum += value
  # Returns sum
  return sum


def maxvalue(values):
  """ The purpose of the function is to find a maximum value in a list.
  The function returns an index of the maximum value
  The function does not use any predefined functions
  Example of input: [1,2,3,4]
  Example of output: 4
  """
  # Assign first element of a list
  max_value = values[0]
  # Loop raises ValueError if not int or float was given in the list 
  for value in values:
    # Check if the element is not a number
    if not isinstance(value, (int, float)):
      raise ValueError("Non-numerical value present in the list")




  # Loop iterates over the elements in the list
  for i in range(1, len(values)):
    # Check if the element is greater than the maximum value
    if values[i] > max_value:
      # Update index and the maximum value
      max_value = values[i]
      index = i

  # Return the index 
  return index




def minvalue(values):
  """ The purpose of the function is to find a minimum value in a list.
  The function returns an index of the minimum value
  The function does not use any predefined functions
  Example of input: [1,2,3,4]
  Example of output: 4
  """
  # Assign first element of a list
  min_value = values[0]
  index = 0
  
  # Loop raises ValueError if not int or float was given in the list 
  for value in values:
    # Check if the element is not a number
    if not isinstance(value, (int, float)):
      raise ValueError("The list contains non-numerical values")


  # Loop iterates over the elements in the list
  for i in range(1, len(values)):
    #Check if the element is less than the minumum value
    if values[i] < min_value:
      # Update index and the minimum value
      min_value = values[i]
      index = i

  print(index)
  # Return the index 
  return index



def meannvalue(values):
  """ The purpose of the function is to find mean of values in the list.
  The function returns mean value.
  The function does not use any predefined functions.
  Example of input: [1,2,3,4,10]
  Example of output: 4
  """

  mean_value = 0
  # Sum of numbers
  sum = 0
  # Loop raises ValueError if not int or float was given in the list 
  for value in values:
    # Check if the element is not a number
      if not isinstance(value,(int, float)):
          raise ValueError('Non numerical value present in a list')
  # Loop sums all values in the list
  for value in values:
      sum += value
  # Calculate mean value
  mean_value = sum/len(values)
  # Return mean value
  return mean_value

        
def countvalue(values,x):
  """ The purpose of the function is to count how many times 'x' appears in a list
  The function returns number of occurences
  The function does not use any predefined functions
  Example of input: countvalue([1,1,2,3],1)
  """
  # Nubmer of occurences
  occurences = 0
  # Loop counts number of occurences
  for value in values:
      if value == x:
        occurences += 1
  # Returns occurences      
  return occurences


