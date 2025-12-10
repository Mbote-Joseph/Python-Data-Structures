name = input("Enter your name:")

# length of the string
print(f"The length of the string is {len(name)}")

# Find the first occurrence
print(name.find(" "))

# Find last occurrence
print(name.rfind("e"))

# Write first letter of the string in capital
print(name.capitalize())

# Upper case
print(name.upper())

# Lower case
print(name.lower())

# Title case
print(name.title())

# Checking if it is digits 
print(name.isdigit())

# Checking if it is alphabets
print(name.isalpha())

# Checking if phone numbers is correct using dashes

phone_number = input("Enter the Phone number:")
if phone_number.count("-") == 3:
    print(f"The phone number {phone_number} is correct")
else:
    print(f"Phone number {phone_number} is not correct")