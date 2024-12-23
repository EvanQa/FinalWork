#Given two arrays of integers. Add up each element in the same position and create a new array containing the sum of each pair.
#Assume both arrays are of the same length.


def sum_of_lists(first_array, second_array):
    result = []
    for i in range(len(first_array)):
        result.append(first_array[i] + second_array[i])
    return result




if __name__ == '__main__':
    first_array = [4, 6, 7]
    second_array = [8, 1, 9]

    result = sum_of_lists(first_array,second_array)
    print(result)