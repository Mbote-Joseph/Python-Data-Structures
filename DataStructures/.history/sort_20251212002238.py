nums = [4,2,3,1,4,6,8,5,3,4,6]

def sort_array(nums):
    sorted_array = []
    for i in range(0, len(nums)):
        least_number = min(nums)
        sorted_array.append(least_number)
        nums.remove(least_number)
    return sorted_array


print(sort_array(nums))