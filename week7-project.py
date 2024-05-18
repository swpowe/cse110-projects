# Project 07: Windchill Calculator
# Your assignment is to write a program that asks the user for a 
# temperature and then shows the wind chill values for various wind speeds at that temperature.

# Your program should compute and display the wind chill for wind speeds of 
# 5, 10, 15, ..., 60 miles per hour, just like the National Weather Service chart does. To help 
# users who are more familiar with Celsius, your program should allow temperature to be entered 
# in either Celsius or Fahrenheit, and if needed, convert the Celsius temperature to Fahrenheit 
# before using the formula.
def get_windchill(temp, speed):
    windchill = 35.74 + (0.6215 * temp) - (35.75 * (speed ** 0.16)) + ((0.4275 * temp) * (speed ** 0.16))
    return windchill #!! placeholder

def convert_celsius(temp_fahrenheit):
    return temp_fahrenheit * (9/5) + 32

def output(temp):
    windchill = 0.00
    # wind_speed = 5
    
    for i in range(5, 65, 5):
        windchill = get_windchill(temp, i)
        print(f"At temperature {temp}F, and wind speed {i} mph, the windchill is: {windchill:.2f}F")


temp = float(input("What is the temperature? "))
scale = input("Fahrenheit or Celsius (F/C)? ").lower()

if scale == "c":
    temp = convert_celsius(temp)

# print(f"At temperature {temp:.1f}, and wind speed 5 mph, the windchill is: {windchill:.2f}F")

output(temp)
