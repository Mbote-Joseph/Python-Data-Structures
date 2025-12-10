# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# username must not contain digits

username = input("Enter your username:")

if username.len() <= 12 and username.count(" ") == 0 and username.isalpha():
    print(f"The username {username} is valid")
else:
    print(f"The username {username} is not valid. It should have less than 12 characters, do not contain spaces and should not contain spaces.")