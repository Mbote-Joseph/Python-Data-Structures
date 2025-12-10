#  Compound Interest calculator

#  A = P(1 + r/n)^t
import math

principle = float(input("Enter the amount you want to borrow:"))
rate = float(input("Enter the interest rate which the Bank offer"))
time = float(input("Enter the time in years you want to borrow the loan:"))

while principle <= 0 or rate <= 0 or time <= 0:
    print("Invalid value")
    principle = float(input("Enter the amount you want to borrow:"))
    rate = float(input("Enter the interest rate which the Bank offer"))
    time = float(input("Enter the time in years you want to borrow the loan:"))
    
amount = principle * (1 + rate/100)**time

print(f"The principle of : ${principle} at a rate of {rate}% for a period of {time} years, The amount repayed will be: ${amount} ")