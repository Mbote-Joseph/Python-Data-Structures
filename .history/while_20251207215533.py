# while loop - Execute some code WHILE some condition remains true

username = input("Enter your username:")

while len(username) < 3 and username.isalpha() and not username.find(" " == -1):
    print(f"The username {username} is INVALID!")
    username = input("Enter your username:")
