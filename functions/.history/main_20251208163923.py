# function - A block of reusable code 
# place () after the function name to call it
name = input("Enter the name of the student: ")

def studentEmail(name):
    print(f"Dear {name}")
    print(f"\nHello {name}, Hope you are doing great. \n\nKind regard,")
    
studentEmail(name)