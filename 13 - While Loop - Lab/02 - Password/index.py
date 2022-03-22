username = str(input())
password = str(input())

while True:
    guess_password = str(input())

    if guess_password == password:
        print(f"Welcome {username}!")
        break