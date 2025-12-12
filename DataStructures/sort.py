nums = [14,52,43,1,24,6,8,15,3,4,76]

def sort_array(nums):
    sorted_array = []
    for i in range(0, len(nums)):
        least_number = min(nums)
        sorted_array.append(least_number)
        nums.remove(least_number)
    return sorted_array


print(sort_array(nums))