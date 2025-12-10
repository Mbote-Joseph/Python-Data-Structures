# Sort

def sort_numbers(numbers):
    sorted_list = []
    for number_index in range(0,numbers):
        if numbers[number_index] > numbers[number_index+1]:
            number = int(numbers[number_index+1])
            sorted_list.append(number)
        else:
            number = int(numbers[number_index])
            sorted_list.append(number)
            
    return sorted_list


number_list = [45,67,98,12,45,67,88,33,12,45,67]

print(number_list)
print(sort_numbers(number_list))