# type: ignore
import array
from numpy import reshape

print("The matrix :")
my_array = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
['Wed',15,21,20,19],['Thu',11,20,22,21],
['Fri',18,17,23,22],['Sat',12,22,20,18],
['Sun',13,15,19,16]])

m = reshape(my_array,(7,5))
print(m)

n = reshape(m, (1,35))
print(n)