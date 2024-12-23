#Write a function to return an array of all the elements that are repeated more than once in a given array.


def return_repeated_elements(arr):
    duplicates = []
    for num in arr:
        if arr.count(num) > 1 and num not in duplicates:
            duplicates.append(num)
    return  duplicates





if __name__ == '__main__':

    arr = [4,2,34,4,1,12,1,4]
    print(return_repeated_elements(arr))