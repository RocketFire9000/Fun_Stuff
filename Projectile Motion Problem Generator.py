import math
from sys import exit
from random import randint
g = 9.8
vo = 0
theta_deg = 0
vo = randint(0, 1000)
theta_deg = randint(0, 90)
theta_rad = theta_deg * 0.01745329  # Turns degrees into radians because the math package's trig functions are in radians
print("Find the following information using the given variables about launching a cannonball: \nDistance from starting point, max height, and time of flight:\nUsing: \ngravity = 9.8 \nvelocity =", vo, "\ndegrees = ", theta_deg, "\nheight = 0")
flight_time = round((2 * vo * math.sin(theta_rad) / g), 2)  # Equation for time of flight
final_distance = round((vo ** 2 * math.sin(2 * theta_rad) / g), 2)  # Equation for max x
final_height = round((vo ** 2) * (math.sin(theta_rad) ** 2) / (2 * g), 2)  # Equation for max y.
if float(input("How long was the cannonball in the air?")) == flight_time:
    print("That is correct! The answer is", flight_time)
else:
    print("That is incorrect! Please try again. The correct answer was", flight_time)
    exit()
if float(input("How far did the cannonball go?")) == final_distance:
     print("That is correct! The answer was", final_distance)
else:
    print("That is incorrect! Please try again. The correct answer is", final_distance)
    exit()
if float(input("How high did the cannonball go?")) == final_height:
     print("That is correct! The answer was", final_height)
else:
    print("That is incorrect! Please try again. The correct answer is", final_height)
    exit()
print("Congradulations! You got it correct! The problem was:\nA cannonball launched at", theta_deg, "degrees, with a speed of", vo,", what would the final distance, height, and time of flight be? Your answer was:\nA time of flight of:",flight_time,"\nA max height of", final_height,"\nAnd a final distance of", final_distance, ".")