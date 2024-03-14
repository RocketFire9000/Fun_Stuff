# Below can double a number a certain amount of times.
c = 0
i = input("Please input a number to be doubled:")
if "." in i:
    i = float(i)
else:
    i = int(i)
ci = input("Please input a whole number to double the first number by:")
ci = int(ci)
print(i, ": Input")
while c < ci:
    i += i
    print(i, ":", "|", float(i / 2), "+", float(i / 2), "| :", "Interation", c + 1)
    c = c + 1
