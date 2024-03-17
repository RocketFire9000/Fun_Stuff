import math
g = 9.8  # m/s^2
vo = int(input("vo: What is the original x velocity? (How fast is it going in meters per second?) "))
theta_deg = int(input("theta: What angle is it being launched in degrees? Max 90. "))
theta_rad = theta_deg * 0.01745329


def round_up(n, decimals=0):
    multiplier = 10**decimals
    return math.ceil(n * multiplier) / multiplier


vo ** 2 * math.sin(2 * theta_rad) / g
t = (2 * vo * math.sin(theta_rad)) / g
print(round(t,2))