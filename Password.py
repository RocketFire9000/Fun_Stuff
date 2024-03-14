from random import randint
import base64


def generate_password(leg):
    random_numbers = str(randint(0, 1))
    for i in range(int(leg)):
        random_numbers += str(randint(0, 9))
    encoded_string = base64.b64encode(random_numbers.encode('utf-8'))
    return encoded_string


print(generate_password(input("Length of password: ")))
