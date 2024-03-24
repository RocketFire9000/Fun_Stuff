import math
from sys import exit
print("This program will graph the trajectory of a cannon ball given the variables below. Please enter any positive integer. Do know that higher values may not be visible on the simulation.")
g = float(input("What is the gravitational constant in meters per second per second that you want to use? Earth's gravity ia ~9.8 m/s^2. "))
vo = int(input("What is the original x velocity? (How fast is it going in meters per second?) "))
theta_deg = int(input("What angle is it being launched in degrees? Max 90. "))
theta_rad = theta_deg * 0.01745329
if vo <= 0 or theta_deg <= 0:
    print("Please only use real, positive numbers.")
    exit()
flight_time = round((2 * vo * math.sin(theta_rad) / g), 2)
final_distance = round((vo ** 2 * math.sin(2 * theta_rad) / g), 2)
final_height = round((vo ** 2) * (math.sin(theta_rad) ** 2) / (2 * g), 2)
print("The cannon ball will land", final_distance, "meters away")
print("The cannon ball reached a height of", final_height, "meters above the ground.")
print("It was in the air for", flight_time, "seconds.")
