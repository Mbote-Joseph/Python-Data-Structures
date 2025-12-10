# while loop - Execute some code WHILE some condition remains true

username = input("Enter your username:")

while len(username) < 3 and username.isalpha():
    print(f"The username {username} is INVALID!")
    username = input("Enter your username:")
