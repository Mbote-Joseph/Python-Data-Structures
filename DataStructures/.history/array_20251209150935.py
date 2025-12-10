# nums - It is an integer of arrays => nums[]
# It returns an array answer => answer[]
# answer[i] is the product of all element of nums[] except nums[i]

nums = [1,2,3,4,5]
# product = 1
answer = []

def product_of_elements_behind_i(nums):
    product = 1
    for i in range(1,len(nums)+1):
        product *= nums[i - 1]
        print(f"The Product upto index {i-1} is : {product}")
        answer.append(product)
    return answer


print(product_of_elements_behind_i(nums))