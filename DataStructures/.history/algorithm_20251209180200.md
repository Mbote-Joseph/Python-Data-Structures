# Algorithm - Set of steps to accomplish a task

- Step 1
- Step 2
- Step 3
- ...

## Types of Algorithms

- Simple recursive algorithms

```py
Algorithm Sum(A, n):
    if n = 1:
        return A[0]
    s = Sum(A, n-1) # recurse on all but last
    s = s + A[n-1] # Add last element
return s
```

- Divide and Conquer algorithms
- Dynamic Programming algorithms
- Greedy algorithms
- Brute force algorithms
- Randomized algorithms
