from random import randint
x = int(input("Length of number: "))
g = int(input("Amount of numbers to generate: "))
i = 0
t = ""
c = 0
while i < g:
    while c < x:
        if c > 0:
            t += str(randint(0, 9))
            c += 1
        else:
            t += str(randint(1, 9))
            c += 1
    i += 1
    print(t)
    t = ""
    c = 0
