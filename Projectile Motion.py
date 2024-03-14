import turtle
from turtle import *
import math
from sys import exit
print("This program will graph the trajectory of a cannon ball given the variables below. Please enter any positive integer. Do know that higher values may not be visible on the simulation.")
g = 9.8  # m/s^2 (make this also changeable?)
vo = int(input("vo: What is the original x velocity? (How fast is it going in meters per second?) "))
theta_deg = int(input("theta: What angle is it being launched in degrees? Max 90. "))
theta_rad = theta_deg * 0.01745329
if vo <= 0 or theta_deg <= 0:
    print("Please only use real, positive numbers.")
    exit()


def round_up(n, decimals=0):
    multiplier = 10**decimals
    return math.ceil(n * multiplier) / multiplier  # Not actually written by me, borrowed from an online tutorial.


final_distance = round_up(vo ** 2 * math.sin(2 * theta_rad) / g, 2)
final_height = round((vo ** 2) * (math.sin(theta_rad) ** 2) / (2 * g), 2)
print("The cannon ball will land", final_distance, "meters away")
print("The cannon ball reached a height of", final_height, "meters above the ground.")
turtle.forward(100)
turtle.forward(100)
turtle.forward(100)
turtle.forward(100)
turtle.forward(100)
turtle.forward(100)
