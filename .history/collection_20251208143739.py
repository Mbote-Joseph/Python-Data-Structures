# collection -  single "variable" used to store multiple values
# List - [] ordered and changeable. Duplicates OK
# Set - {} unordered and immutable, but Add/Remove OK. No duplicates
# Tuple - () ordered and unchangeable. Duplicates OK. Faster

subjects = ["Mathematics", "English", "Kiswahili", "Physics", "Chemistry","Geography", "Computer Studies"]


subjects.insert(3, "Biology")

subjects.sort()
subjects.reverse()

for subject in subjects:
    print(f"{subject.title()}")


print("======Fruits Tuple==========")
# Fruits
fruits = {"apple","Banana","coconut","mango","mango"}

for fruit in fruits:
    print(fruit)