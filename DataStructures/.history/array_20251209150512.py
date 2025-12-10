# nums - It is an integer of arrays => nums[]
# It returns an array answer => answer[]
# answer[i] is the product of all element of nums[] except nums[i]

nums = [1,2,3,4,5]
answer = []

def product_of_elements_behind_i(nums):
    for i in range(1,len(nums)):
        product *= nums[i-1]
        answer.append(answer)
    return answer
