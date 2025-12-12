nums = [14,52,43,1,24,6,8,15,3,4,76]

def merger_sort(nums):
    half_total_numbers = int(len(nums)/2)
    left_half = []
    right_half = []
    for x in range(0, half_total_numbers):
        left_half = left_half.append(nums[x])
        merger_sort(left_half)
        
    for x in range(half_total_numbers, len(nums)):
        right_half = right_half.append(nums[x])
        merger_sort(right_half)
        
    
        
    return left_half, right_half

print(merger_sort(nums))