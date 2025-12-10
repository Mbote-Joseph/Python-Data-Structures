# Variable - A container for a value (String, integer, float, boolean). It behaves as if it was the value that it contains.

# Strings
first_name = "Joseph"
food = "Pizza"
email = "josephmbote@gmail.com"

# Integers
age = 21
number_of_friends = 5

# Floats
height = 5.9
gpa = 4.0

# Boolean
is_active = True
is_enrolled = False

print(f"Hello {first_name}, you like {food}")
print(f"Your email is {email}")
print(f"You are {age} years old")
print(f"You are {height} feet tall")
print(f"You have {number_of_friends} friends")
print(f"Your GPA is {gpa}")

if is_active:
    print("You are active")
    if is_enrolled:
        print("You are enrolled")
    else:
        print("You are not enrolled")
else:
    print("You are not active")


# Task
user_name = "Mbote-Joseph"
year = 2025
pi = 3.14159
is_admin = True

print(f"Hello {user_name}, you are in {year}")
print(f"Pi is {pi}")
if is_admin:
    print("You are an admin")
else:
    print("You are not an admin")