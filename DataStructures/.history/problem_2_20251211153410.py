nums = [3,2,5,0,1,7,0,9,8]

def zero_movers(nums):
    zeros = []
    # zeros.
    for i in range(0, len(nums)):
        if nums[i] == 0:
            zeros.insert[nums[i]]
            nums = filter(lambda x: x != nums[i])
        
    final_array = nums + zeros
    
    return final_array


print(zero_movers(nums))