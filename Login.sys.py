def login_sys(username, password):
    with open("UserData", 'r') as file:
        lines = file.readlines()
    username_data = lines[0].replace("Username: ", "").strip()
    password_data = lines[1].replace("Password: ", "").strip()
    if username == username_data and password == password_data:
        return True
    else:
        return False


print("Login")
if login_sys(input("Username:"), input("Password:")):
    print("Login successful!")
else:
    print("Either the password or username was incorrect.")
    print("Login")
    login_sys(input("Username:"), input("Password:"))
