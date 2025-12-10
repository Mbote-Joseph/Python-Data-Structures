def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fibonacci(n-1)
    

number = int(input("Enter the number you want to find the fibonacci number: "))
print(f"The fibonacci of {number} is : {fibonacci(number)} ")