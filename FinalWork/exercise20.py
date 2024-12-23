#Use a while loop to iterate on a boolean array.
#As long as the next index is different from the previous index the iteration
#continues, otherwise, return the index of the element with the same value.
#If there are not two successive values, the function will return-1.

def find_consecutive_duplicate(arr):
    i = 1
    while i < len(arr):
        if arr[i] == arr[i - 1]:
            return i
        i += 1
    return -1

array1 = [True, False, False, True, True, False]
array2 = [True, False, True, False, True, True]
array3 = [True, False, True, False, True, False]

print(find_consecutive_duplicate(array1))
print(find_consecutive_duplicate(array2))
print(find_consecutive_duplicate(array3))
