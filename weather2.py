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
    
    # find min 
    # iterate over each list in list, then 1st loop is list.
    min_list = []
    max_list = []
    for day in weather_data: 
        min_list.append(day[1])
        max_list.append(day[2])

    # print(min_list)
    min_value, min_position = find_min(min_list)
    # print(min_value)
    # print(min_position)

    # extract timestamp from min_position list. 
    min_timestamp = weather_data[min_position][0] # -> lists[b][a] gets the element in index a from the list in index b in lists
    # print(min_timestamp)

    # convert min_value to celcius
    min_value = convert_f_to_c(min_value)
    # print(min_value)

    # convert min_timestamp to min_date
    min_date = convert_date(min_timestamp)
    # print(min_date)

    #print(f"{len(weather_data)} Day Overview \nThe lowest temperature will be {format_temperature(min_value)} on {min_date} ") # we need to put everything into 1 line. 

    overview = f"{len(weather_data)} Day Overview\n"
    line_low = f"  The lowest temperature will be {format_temperature(min_value)}, and will occur on {min_date}.\n" 

#   Find max
# iterate over each list in list, then 1st loop is list.
    # max_list = []
    # for day in weather_data: 
    #     max_list.append(day[2])
    # print(max_list)
    max_value, max_position = find_max(max_list)
    # print(max_value)
    # print(max_position)

    # extract timestamp from max_position list. 
    max_timestamp = weather_data[max_position][0] # -> lists[b][a] gets the element in index a from the list in index b in lists
    # print(max_timestamp)

    # convert max_value to celcius
    max_value = convert_f_to_c(max_value)
    # print(max_value)

    # convert max_timestamp to max_date
    max_date = convert_date(max_timestamp)
    # print(max_date)

    #print(f"The highest temperature will be {format_temperature(max_value)} on {max_date} ")
    line_high = f"  The highest temperature will be {format_temperature(max_value)}, and will occur on {max_date}.\n"

    # find average low - The average low this week is 12.2°C. function = calculate_mean(weather_data)
    
    lows = []
    for day in weather_data:
        lows.append(day[1]) # this is the index 1 NOT weather_data[1]!!!!! To get the min column in the CSV
    # print(lows)

    average_low = calculate_mean(lows)
    # print(average_low)

    # convert average_low to celcius
    average_low = convert_f_to_c(average_low)

    # print(f"The average low this week is {format_temperature(average_low)}")
    line_avg_low = f"  The average low this week is {format_temperature(average_low)}.\n"


    # find average high - The average high this week is 17.8°C.
    highs = []
    for day in weather_data:
        highs.append(day[2]) # this is the index 2 NOT weather_data[2]!!!!! To get the max column in the CSV
    # print(highs)

    average_high = calculate_mean(highs)
    # print(average_high)

    # convert average_low to celcius
    average_high = convert_f_to_c(average_high)

    # print(f"The average high this week is {format_temperature(average_high)}")
    line_avg_high = f"  The average high this week is {format_temperature(average_high)}.\n"

    summary = overview + line_low + line_high + line_avg_low + line_avg_high
    return summary



# example = [
#              ["2021-07-02T07:00:00+08:00", 100, 67],
#              ["2021-07-03T07:00:00+08:00", 57, 68],
#              ["2021-07-04T07:00:00+08:00", 56, 62],
#              ["2021-07-05T07:00:00+08:00", 55, 61],
#              ["2021-07-06T07:00:00+08:00", 53, 62]
#          ]
# print(generate_summary(example))

# 8 Day Overview
# The lowest temperature will be -46.7°C, and will occur on Tuesday 23 June 2020.
#  The highest temperature will be 22.2°C, and will occur on Sunday 21 June 2020.
#  The average low this week is -16.1°C.
#  The average high this week is 12.4°C.

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary = ""
    for day in weather_data:
        # format date
        current_date = convert_date(day[0])
        summary += f"---- {current_date} ----\n"

        # format min temp
        min_temp = day[1]
        converted_min_temp = format_temperature(convert_f_to_c(min_temp))
        summary += f"  Minimum Temperature: {converted_min_temp}\n"

        # format max temp
        max_temp = day[2]
        converted_max_temp = format_temperature(convert_f_to_c(max_temp))
        summary += f"  Maximum Temperature: {converted_max_temp}\n\n"

    return summary 


   
# example = [
#               ["2021-07-02T07:00:00+08:00", 100, 67],
#               ["2021-07-03T07:00:00+08:00", 57, 68],
#               ["2021-07-04T07:00:00+08:00", 56, 62],
#               ["2021-07-05T07:00:00+08:00", 55, 61],
#               ["2021-07-06T07:00:00+08:00", 53, 62]
#           ]
# print(generate_daily_summary(example))

# plan: 
# Create empty list
# find daily_date aka the list of all the dates (which are automatically listed in order)
# issue - I want to create a loop of date, min temp and max temp, then loop them for every loop in order of date. 
# idea - for every DAY in WEATHER DATA
# day[0] = convert_date(day[0])
# 
# 
# every item in a list to be printed out individually


# ---- Friday 19 June 2020 ----
#  Minimum Temperature: 8.3°C
#  Maximum Temperature: 7.8°C

#---- Saturday 20 June 2020 ----
#  Minimum Temperature: 10.6°C
#  Maximum Temperature: 19.4°C

# Redoing entire test again....
#  
import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"

x = "hello_world"
print(x)

def format_temperature(temp):
    # to return the temp with the celcius sign after it, just make a one line f string.
    return f"{temp}{DEGREE_SYMBOL}"
print(format_temperature(30)) # 30°C

def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    result = datetime.fromisoformat(iso_string)
    date = result.strftime("%A" "%d" "%B" "%Y")
    return(date) # return the final answer
print(convert_date("2021-07-06T00:00:00")) # Friday, 17 October 2025 1:38:03 PM

def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    temp = (temp_in_fahrenheit - 32) * 5/9
    temp = float(temp)
    rounded_number = round(temp)
    return rounded_number
print(convert_f_to_c(65))

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    
    total = 0.0
    for temp in weather_data:
        total += float(temp) # convert each value to a float and add it
    result = total/ len(weather_data)
    return result


    # temp = len(weather_data) - returns error because it needed to be converted
    # get_sum = sum(weather_data)
    # mean = get_sum/ temp
    # return mean 

weather_data = [20,30,15,29,30]
print(calculate_mean(weather_data))


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data = []
    with open(csv_file, "r", newline = "") as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        for row in csv_reader:
            if not row:
                continue
            date = row[0]
            min_temp = int(row[1])
            max_temp = int(row[2])
            data.append([date,min_temp,max_temp])
    return data

# you have to convert two numbers to integers here so you do it here instead of later on. 
# Therefore  data.append(row) doesn't work because it doesn't convert. 
# it also asks you to return a list therefore all 3 are in brackets in ().
# data.append([date,min_temp,max_temp]) means making and transplanting a list into a bigger list of lists. 

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return()
    # if there is no data in list, return an empty tuple (not list)
    min_value = float(weather_data[0])
    min_position = 0

    # Assume that the lowest number is 8, in position 0. Therefore:
    # min_value = 8
    # min_position = 0.


    for i in range(1, len(weather_data)):
    # for every position number i in my list of weather data
    # We start from position 1 because 0 is already covered. 
    # We need the length of the weather_data list to get a number for the number of items. We have 7 items. Therefore len(weather_data) = 7
    # So the range is between position 1 (3) and the number before the end of the list. Range(1, 7) =  1,2,3,4,5,6 as it stops before 7.  

        value = float(weather_data[i]) # get the value at the current index and convert it to a float so 3 becomes 3.0

        if value <= min_value:
            min_value = value
            min_position = i

    # Now it loops through the values. If the first item (value) is less than or equal to the first item we find, then the min_value is the NEW value. 
    # Once it locks in the min_value, the min_posistion is recorded at the same time.

    # if the index in the list is greater than last index, index = bigger index. 
    return min_value, min_position

    # min_value = min(weather_data)
    # min_position = weather_data.index(min_value) - dont use because index stops at the first match. 

weather_data = [8, 3, 5, 1, 9, 12, 1]
print(find_min(weather_data)) # (1.0, 6)


# ALTERNATIVE CALCULATION!!!!!!!!!!
def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and its position in the list.
        (In case of multiple matches, return the index of the *last* example.)
    """
    if not weather_data:
        return ()

    # Start by assuming the first value is the minimum.
    min_value = float(weather_data[0])
    min_position = 0

    # Enumerate gives you both index (i) and value automatically.
    for i, value in enumerate(weather_data):
        value = float(value)
        if value <= min_value: # less than or equal to
            min_value = value
            min_position = i

    return min_value, min_position

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and its position in the list.
        (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return () or None

    # Start by assuming the first value is the maximum.
    max_value = float(weather_data[0])
    max_position = 0

    # Enumerate gives you both index (i) and value automatically.
    for i, value in enumerate(weather_data):
        value = float(value)
        if value >= max_value: # greater than or equal to
            max_value = value
            max_position = i

    return max_value, max_position

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    
    min_list = []
    max_list = []
    for day in weather_data: 
        min_list.append(day[1])
        max_list.append(day[2])


    min_value, min_position = find_min(min_list)
    min_timestamp = weather_data[min_position][0] 
    min_value = convert_f_to_c(min_value)
    min_date = convert_date(min_timestamp)

    overview = f"{len(weather_data)} Day Overview\n"
    line_low = f"  The lowest temperature will be {format_temperature(min_value)}, and will occur on {min_date}.\n" 

    max_value, max_position = find_max(max_list)
    max_timestamp = weather_data[max_position][0] 
    max_value = convert_f_to_c(max_value)
    max_date = convert_date(max_timestamp)
    line_high = f"  The highest temperature will be {format_temperature(max_value)}, and will occur on {max_date}.\n"
    
    lows = []
    for day in weather_data:
        lows.append(day[1]) 

    average_low = calculate_mean(lows)
    average_low = convert_f_to_c(average_low)
    line_avg_low = f"  The average low this week is {format_temperature(average_low)}.\n"

    highs = []
    for day in weather_data:
        highs.append(day[2]) 

    average_high = calculate_mean(highs)
    average_high = convert_f_to_c(average_high)
    line_avg_high = f"  The average high this week is {format_temperature(average_high)}.\n"

    summary = overview + line_low + line_high + line_avg_low + line_avg_high
    return summary



def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary = ""
    for day in weather_data:
        current_date = convert_date(day[0])
        summary += f"---- {current_date} ----\n"

        min_temp = day[1]
        converted_min_temp = format_temperature(convert_f_to_c(min_temp))
        summary += f"  Minimum Temperature: {converted_min_temp}\n"

        max_temp = day[2]
        converted_max_temp = format_temperature(convert_f_to_c(max_temp))
        summary += f"  Maximum Temperature: {converted_max_temp}\n\n"

    return summary 

