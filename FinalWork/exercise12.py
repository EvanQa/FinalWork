#Write a function using a for loop that gets an array and returns a new array
#with the elements from the given array appearing in reverse order. (Don’t use array reverse() method)






def reverse_list(arr):
    reverse_array = []
    for i in range(len(arr) -1, -1, -1):
        reverse_array.append(arr[i])
    return reverse_array






if __name__ == '__main__':

    arr = [43, "what", 9, True, "cannot", False, "be", 3, True]
    reverse_array = reverse_list(arr)

    print("List before shifting", arr)
    print("List after shifting", reverse_array)