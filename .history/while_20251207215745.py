# while loop - Execute some code WHILE some condition remains true

username = input("Enter your username:")

while len(username) < 3 or not username.isalpha() or not username.find(" " == -1):
    print(f"The username {username} is INVALID!")
    username = input("Enter your username:")

print(f"Hello {username}")