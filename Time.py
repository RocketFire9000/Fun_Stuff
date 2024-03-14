import time
while True:
    timeprint = time.strftime("%m/%d/%Y|%H:%M:%S")
    print(f"\r |{timeprint}|", end="")
