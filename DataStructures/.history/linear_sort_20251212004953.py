nums = [14,52,43,1,24,6,8,15,3,4,76]

def linear_sort(nums):
    sorted_arr = []
    for i in range(len(nums)):
        temp = nums[i]
        if temp > nums[i]:
            temp = nums[i]
            nums.remove(temp)
        sorted_arr.append(temp)
    return sorted_arr
            
print(linear_sort(nums))