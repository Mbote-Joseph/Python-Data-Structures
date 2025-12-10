# Array is a container, which can hold a fixed number of items of the same type.
# Array has:
    #  Element - Each item stored in an array is called an element.
    #  Each location of an element in an array has a numerical index, which s used to identify the element.
    
# Basic Operations
# - The basic operations supported by an array are:
    # Traverse - Print all the array elements one by one.
    # Insertion - Adds an element at a given index
    # Deletion - Deletes an element at a given index
    # Search - Searches an element, using the given index or by value.
    # update - Update an element at a given index.




units = ["Maths","English","Kiswahili","Chemistry","Physics","Geography","Computer"]
scores = [87,98,75,67,99,45,34]


def print_report(units, scores):
    total_score = 0
    for i in range(0, len(units)):
        total_units = len(units)
        total_subject_scores = len(scores)
        grade = ""
        total_score += scores[i]
        if total_units == total_subject_scores:
            if 70<=scores[i] <= 100 :
                grade = "A"
            elif scores[i] >=60:
                grade = "B"
            elif scores[i] >= 50:
                grade = "C"
            elif scores[i] >= 40:
                grade = "D"
            elif 0<= scores[i] < 40:
                grade = "E"
            else:
                grade = "Invalid Score"
            
            print(f"{units[i]} - {scores[i]} - {grade}")
            
    print(f"Total Score : {total_score}")
    
def add_unit_and_score(units, scores):
    unit = input("Enter the Unit you want to add: ")
    score = int(input("Enter the score of the unit you added:"))
    units.insert(len(units), unit)
    scores.insert(len(scores), score)
    
    return units, scores

def menu():
    print("==================================================================")
    print("================= Welcome to Mbote Senior School==================")
    print("==================================================================")
    print("1. Print the Student Report: ")
    print("2. Add extra units for the student: ")
    print("3. Remove a units from the student: ")
    print("4. Update units/score from the student: ")
    print("0. Exit the system ")


def exit():
    print("===================================================================")
    print("===============Thank you for Trusting our System===================")
    print("===================================================================")


def delete_unit(units, scores):
    for unit in range(0,len(units)):
        print(f"{unit+1}. {units[unit]}")
    
    choice = int(input("Enter the number of the unit you want to delete(1,2,3,4,5,6,7,8,9...): "))
    units.remove(units[choice-1])
    scores.remove(scores[choice-1])
    
    return units, scores


def update_unit(units, scores):
    for unit in range(0,len(units)):
        print(f"{unit+1}. {units[unit]} - {scores[unit]}")
    option = input("Enter the index of the unit you want to update: ")
    name = int(input(f"Enter the correct name for {units[option - 1]}: "))
    units[option-1] = name
    
    return scores

def update_score(units, scores):
    for unit in range(0,len(units)):
        print(f"{unit+1}. {units[unit]} - {scores[unit]}")
    option = int(input("Enter the index of the unit you want to update the score: "))
    score = int(input(f"Enter the correct score for {units[option - 1]}: "))
    scores[option-1] = score
    
    return scores

def update(units, scores):
    print("1. Unit name")
    print("2. Score")
    option = int(input("You want to update Unit name or score ? (1, 2):"))
    match option:
        case 1:
            update_unit(units, scores)
        case 2:
            update_score(units, scores)
        case 0:
            print("Invalid choice")
            exit()
    

while True:
    menu()
    operation = int(input("\nEnter the operation you want to conduct(1, 2, 3, 4, 5, 0): "))
    
    match operation:
        case 1:
            print_report(units, scores)
        case 2:
            add_unit_and_score(units, scores)
        case 3:
            delete_unit(units, scores)
        case 4:
            update(units, scores)
        case 0:
            exit()
            break
