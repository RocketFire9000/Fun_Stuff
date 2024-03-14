from random import randint
w = 0
l = []
i = 0
while w < 1:
    w += randint(-1, 1)
    l.append(w)
    i += 1
    print(w)
print("Lowest score achieved:", min(l))
print("It took", i, "iteration(s) to get to 1.")