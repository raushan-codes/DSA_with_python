def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last)//2 
        """two division operator is called floor division operator.. rounds to the lower whole number. For example - 3.5 to 3"""

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in the list.")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 10)
verify(result)

""" Note that if the list is not sorted, the algo is not able to produce the desired result"""
