# [12,34,56,77,89,23,45,56]


def linear_search(n, arr):
    for i in range(0,len(arr)):
        if arr[i] == n:
            return i
    return -1
        
array = [12,34,56,77,89,23,45,59]

print(linear_search(59, array))

def merge_search(n, arr):
    half = int(len(arr)/2)
    for i in range(0, half):
        if arr[i] == n:
            return i
        else:
            print("Not in first Half")
            for j in range(half, len(arr)):
                if arr[j] == n:
                    return j
    return -1

print(merge_search(59, array))