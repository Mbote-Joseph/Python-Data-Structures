 # type: ignore
import numpy as np 

print("The matrix :")
# We use np.array explicitly
my_array = np.array([
    ['Mon', 18, 20, 22, 17],
    ['Tue', 11, 18, 21, 18],
    ['Wed', 15, 21, 20, 19],
    ['Thu', 11, 20, 22, 21],
    ['Fri', 18, 17, 23, 22],
    ['Sat', 12, 22, 20, 18],
    ['Sun', 13, 15, 19, 16]
])

# NOTE: Numbers will still be strings because of the 'Mon'/'Tue' labels.
# If you want mixed types (strings AND numbers), use Pandas instead of NumPy.

m = my_array.reshape(7, 5)
print(m)

n = m.reshape(1, 35)
print(n)