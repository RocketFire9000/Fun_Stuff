x = int(input("What number do you want to be factorial? "))
final_x = x
counter = 1
while counter < x:
    final_x = counter * final_x
    counter += 1
if x == 0:
    final_x = 1
elif x < 0:
    final_x = "Error! A number less than 0 can not be factorial!"
print(final_x)
