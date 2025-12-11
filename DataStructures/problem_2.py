nums = [3,2,5,0,1,7,0,9,8]

def zero_movers(nums):
    zeros = list(filter(lambda x: x == 0, nums))
    non_zeros = list(filter(lambda x: x != 0, nums))
    
    final_array = non_zeros + zeros
    
    return final_array


print(zero_movers(nums))