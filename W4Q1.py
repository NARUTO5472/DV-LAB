import pandas as pd

# List of temperatures for a week (in Celsius)
temperatures = [22, 25, 21, 23, 26, 24, 22]

# Assigning index labels as days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Creating a Pandas Series
temperature_series = pd.Series(temperatures, index=days)

# a. Find and print the average (mean) temperature for the week
average_temp = temperature_series.mean()
print("Average Temperature:", average_temp)

# b. Identify and print the maximum and minimum temperatures and their respective days
max_temp = temperature_series.max()
min_temp = temperature_series.min()
max_day = temperature_series.idxmax()
min_day = temperature_series.idxmin()
print(f"Maximum Temperature: {max_temp}°C on {max_day}")
print(f"Minimum Temperature: {min_temp}°C on {min_day}")

# c. Display the temperatures greater than a specific value (e.g., 23°C)
specific_value = 23
higher_temps = temperature_series[temperature_series > specific_value]
print(f"Temperatures greater than {specific_value}°C:\n{higher_temps}")

# d. Convert all temperatures to Fahrenheit (°F = °C * 9/5 + 32)
temperature_fahrenheit = temperature_series * 9/5 + 32
print("Temperatures in Fahrenheit:\n", temperature_fahrenheit)

# e. Print the days that had temperatures above the average
above_average_days = temperature_series[temperature_series > average_temp]
print("Days with temperatures above the average:\n", above_average_days)
