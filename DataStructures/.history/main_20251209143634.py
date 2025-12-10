# [12,34,56,77,89,23,45,56]


def linear_search(n, arr):
    for i in range(0,len(arr)):
        if arr[i] == n:
            return i
    return -1
        
array = [12,34,56,77,89,23,45,59]

print(linear_search(59, array))