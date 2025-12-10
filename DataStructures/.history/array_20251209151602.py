# nums - It is an integer of arrays => nums[]
# It returns an array answer => answer[]
# answer[i] is the product of all element of nums[] except nums[i]

nums = [1,2,3,4,5]
# product = 1
answer = []

def product_of_elements_behind_i(nums):
    product = 1
    for i in range(1,len(nums)+1):
        if i == 0:
            product = 1
            answer.append(product)
        elif i == 1:
            product *= nums[0]
            answer.append(product)
        else:
            product *= nums[i - 2]
            print(f"The Product upto index {i-1} is : {product}")
            answer.append(product)
    return answer


print(product_of_elements_behind_i(nums))