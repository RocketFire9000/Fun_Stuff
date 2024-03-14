while True:
    x = eval(input())
    if x // 1 - x % 1 > 0:
        print(int(x))
    else:
        print(float(x))