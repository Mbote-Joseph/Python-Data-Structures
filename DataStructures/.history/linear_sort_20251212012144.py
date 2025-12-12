nums = [14,52,43,1,24,6,8,15,3,4,76]

def linear_sort(nums):
    sorted_arr = []
    for num in nums:
        temp = nums[0]
        if temp > num:
            temp = num
            print(temp)
            # nums.remove(temp)
        sorted_arr.append(temp)
    return sorted_arr
            
print(linear_sort(nums))