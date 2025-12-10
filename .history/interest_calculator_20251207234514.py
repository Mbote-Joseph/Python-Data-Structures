#  Compound Interest calculator

#  A = P(1 + r/n)^t
import math

principle = float(input("Enter the amount you want to borrow:"))
rate = float(input("Enter the interest rate which the Bank offer"))
time = float(input("Enter the time in years you want to borrow the loan:"))

while principle <= 0:
    principle = float(input("Enter the amount you want to borrow:"))
    if principle < 0:
        print("Principle can not be less than zero")
        
while rate <= 0:
    rate = float(input("Enter the interest rate which the Bank offer:"))
    if rate < 0:
        print("Rate can not be less than zero")
        
while time <= 0:
    time = float(input("Enter the time in years you want to borrow the loan:"))
    if time < 0:
        print("Time can not be less than zero")
        
    
    
amount = principle * (1 + rate/100)**time

print(f"The principle of : ${principle} at a rate of {rate}% for a period of {time} years, The amount re-payed will be: ${amount:.4f} ")