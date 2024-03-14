
with open("UserData", 'r') as file:
    lines = file.readlines()
username_data = lines[0].replace("Username: ", "").strip()
password_data = lines[1].replace("Password: ", "").strip()

