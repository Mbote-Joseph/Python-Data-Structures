# Array is a container, which can hold a fixed number of items of the same type.
# Array has:
    #  Element - Each item stored in an array is called an element.
    #  Each location of an element in an array has a numerical index, which s used to identify the element.
    
# Basic Operations
# - The basic operations supported by an array are:
    # Traverse - Print all the array elements one by one.
    # Insertion - Adds an element at a given index
    # Deletion - Deletes an element at a given index
    # Search - Searches an element, using the given index or by value.
    # update - Update an element at a given index.



from array import array


units = array["Maths","English","Kiswahili","Chemistry","Physics","Geography","Computer"]
scores = array[87,98,75,67,99,45,34]


for i in units:
    print(units[i])