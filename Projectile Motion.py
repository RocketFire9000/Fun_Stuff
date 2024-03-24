import math
from sys import exit
print("This program will calculate the trajectory of a cannon ball given the variables below and output the distance the cannonball went, the max height it reached, and how long it was in the air.\n")
g = float(input("What gravitational constant do you want to use? Earth's gravity is ~9.8 m/s^2. Min is >0.\n"))  # Gravity
vo = float(input("What is the original x velocity? Min is > 0.\n"))  # Original Velocity
theta_deg = float(input("What angle is it being launched at? Max 90, min >0.\n"))  # Degrees from horizontal to aim the "cannon"
theta_rad = theta_deg * 0.01745329  # Turns degrees into radians because the math package's trig functions are in radians
if vo <= 0 or theta_deg <= 0 or theta_deg > 90 or g <= 0:  # Making sure all values are in a range that will not produce any abnormal results.
    print("Please only use real, positive numbers.")
    exit()  # Exits the program if any entered values would cause an abnormal result.
flight_time = round((2 * vo * math.sin(theta_rad) / g), 2)  # Equation for time of flight
final_distance = round((vo ** 2 * math.sin(2 * theta_rad) / g), 2)  # Equation for max x
final_height = round((vo ** 2) * (math.sin(theta_rad) ** 2) / (2 * g), 2)  # Equation for max y.
print("The cannon ball will land", final_distance, "meters away")
print("The cannon ball reached a height of", final_height, "meters above the ground.")
print("It was in the air for", flight_time, "seconds.")
