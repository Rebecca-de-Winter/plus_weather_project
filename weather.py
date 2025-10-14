import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    result = datetime.fromisoformat(iso_string)
    formatted_date = result.strftime("%A %d %B %Y")
    return(formatted_date)
# %A = full weekday name
# b = month full name, d = date
# %Y = year https://www.geeksforgeeks.org/python/python-strftime-function/



def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    temp = float(temp_in_fahrenheit)
    celcius = (temp - 32) * 5/9
    rounded_number = round(celcius, 1)
    return(rounded_number)



def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    total = 0
    for temp in weather_data:
        total = total + float(temp)
    result = total/ len(weather_data)
    return result

    # float_list = list(map(float, weather_data)) #map - aka transform. will transform everything that it iterates over in this case weather_data to a float. 
    # result = sum(float_list) / (len(float_list))
    # return(result)


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data_list = []
    with open(csv_file, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            if not row:
                continue
            date = row[0]
            min = int(row[1])
            max = int(row[2])
            data_list.append([date, min, max])
    return data_list 



def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return() # or None, None
    min_value = float(weather_data[0])
    min_position = 0

    for i in range (1, len(weather_data)):
        value = float(weather_data[i])
        if value <= min_value:
            min_value = value
            min_position = i

    return (min_value, min_position)
    
    
    


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return() # or None, None - this means if an empty list is passed you exit early and return nothing
    max_value = float(weather_data[0]) # change to a float. Assume first number is the biggest. max_value is the first number in the list. eg [17.5, 22.3, 18.9, 22.3] therefore [0]= 17.5
    max_position = 0 # eg max_value = 17.5 and its position is 0 aka the first value at the first position. (17.5, 0)

    for i in range (1, len(weather_data)): # loop through the rest of the list starting from index 1 (we've already checked 0) until the end 
        value = float(weather_data[i]) # convert each item in weather_data to a float and store it as a variable so you don't have to convert everything as a float later on. 
        if value >= max_value: # Use >= eg is 23.3 >= 23.3? Yes its equal, but we want to use the second position in the list (position 3). Therefore answer is (22.3,3)
            max_value = value # if we are using position 3 instead of position 1,  
            max_position = i # i = the position we are looping through eg 0,1,2,3. i for index. 
    return (max_value, max_position)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    
    min_value, min_position = find_min(weather_data)
    print(f"min_value: {min_value}")
    print(f"min_position: {min_position}")

    return (f"5 Day Overview \nThe lowest temperature will be {format_temperature(min_value)}")
example = [
            ["2021-07-02T07:00:00+08:00", 49, 67],
            ["2021-07-03T07:00:00+08:00", 57, 68],
            ["2021-07-04T07:00:00+08:00", 56, 62],
            ["2021-07-05T07:00:00+08:00", 55, 61],
            ["2021-07-06T07:00:00+08:00", 53, 62]
        ]
print(generate_summary(example))

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
