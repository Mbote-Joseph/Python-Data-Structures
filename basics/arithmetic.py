# GPA calculator

units = int(input("Enter the number of units: "))
total_grade = 0

unit_grades = []

for i in range(units):
    grade = input("Enter the grade of unit " + str(i + 1) + ": ")
    unit_grades.append(grade)

    if grade == 'A':
        total_grade += 4.0
    elif grade == 'B':
        total_grade += 3.0
    elif grade == 'C':
        total_grade += 2.0
    elif grade == 'D':
        total_grade += 1.0
    elif grade == 'F':
        total_grade += 0.0

print("Your GPA is " + str(total_grade / units))
