# Written by Isaiah Cox, finished 1/24/2023
a = input("Input:")
a = float(a) if '.' in a else int(a)
# Takes an input and changes it into an integer or float.
b = ""
c = ""
d = ""
e = ""
f = ""
# Sets empty variables as placeholders for later.
if isinstance(a, float):
    c = "decimal "
# Prints if "a" is a float.
else:
    if a % 2 == 1:
        d = "odd "
    # Prints if "a" is odd.
    else:
        if a % 2 == 0:
            e = "even "
# Prints if "a" is even.
if a < 0:
    f = "and negative "
# Prints if "a" is negative.
if a != 0:
    print(a, "is", b + c + d + e + f)
if a == 0:
    print("Error. 0 is neither negative nor positive.")
# Prints all detections on one line.

# TODO: prime numbers, make a calculator from scratch.
