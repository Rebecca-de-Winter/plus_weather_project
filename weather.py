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
    total = 0.0
    for temp in weather_data:
        total += float(temp) 
    result = total/ len(weather_data)
    return result


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data_list = []
    with open(csv_file, 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
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
        return() 
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
        return() 
    max_value = float(weather_data[0]) 
    max_position = 0 

    for i in range (1, len(weather_data)): 
        value = float(weather_data[i]) 
        if value >= max_value: 
            max_value = value 
            max_position = i 
    return (max_value, max_position)


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

    # Finding the minimum
    min_value, min_position = find_min(min_list)
    min_timestamp = weather_data[min_position][0] 
    min_value = convert_f_to_c(min_value)
    min_date = convert_date(min_timestamp)

    overview = f"{len(weather_data)} Day Overview\n"
    line_low = f"  The lowest temperature will be {format_temperature(min_value)}, and will occur on {min_date}.\n" 

    # Finding the maximum
    max_value, max_position = find_max(max_list)
    max_timestamp = weather_data[max_position][0] 
    max_value = convert_f_to_c(max_value)
    max_date = convert_date(max_timestamp)
    line_high = f"  The highest temperature will be {format_temperature(max_value)}, and will occur on {max_date}.\n"
    
    # Finding the averages
    average_low = calculate_mean(min_list)
    average_low = convert_f_to_c(average_low)
    line_avg_low = f"  The average low this week is {format_temperature(average_low)}.\n"


    average_high = calculate_mean(max_list)
    average_high = convert_f_to_c(average_high)
    line_avg_high = f"  The average high this week is {format_temperature(average_high)}.\n"

    # Create the final summary
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

