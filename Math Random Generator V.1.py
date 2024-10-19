from random import randint
while True:
    x = randint(0, 10)
    x2 = randint(0, 100)
    print(str(x) + "^" + str(x2))
    a = x ** x2
    ua = int(input())
    if ua == a:
        print("Yes")
    else:
        print("No. Answer is", str(a) + ". You were", abs(a - ua), "off.")
