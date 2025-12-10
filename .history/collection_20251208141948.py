# collection -  single "variable" used to store multiple values
# List - [] ordered and changeable. Duplicates OK
# Set - {} unordered and immutable, but Add/Remove OK. No duplicates
# Tuple - () ordered and unchangeable. Duplicates OK. Faster

subjects = ["Mathematics", "English", "Kiswahili", "Physics", "Chemistry","Geography", "Computer Studies"]

for subject in subjects:
    print(f"{subject}")