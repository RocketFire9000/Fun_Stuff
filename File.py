c = 3
i = 1
print("|Login|")
print("You have", c, "attempts remaining. After", c, "attempts, the account will be deleted. \n")
while i <= 3:
    input("Username: ")
    input("Password: ")
    print("You have", c - i, "attempts remaining.")
    i += 1
print("\nError. Account breach detected, deleting account.")
answer = input("Would you like to create a new account? y/n ")
if answer == "y":
    print("Account has been created. Please perform the following steps to finish setting up your account.")
    username = input("Please input a new username: ")
    password = input("Please input a new password: ")
else:
    print("Error. Input not recognized or all accounts have been permanently deleted. ")
c = 3
i = 1
print("|Login|")
print("You have", c, "attempts remaining. After", c, "attempts, the account will be deleted. \n")
x1 = ""
x2 = ""
while i <= 3 and x1 != username and x2 != password:
    x1 = input("Username: ")
    x2 = input("Password: ")
    print("You have", c - i, "attempts remaining.")
    i += 1
if x1 == username and x2 == password:
    print("Login successful!")
