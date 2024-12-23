#Write a function that prints all the elements of a 2D array using nested for loops.

def matrix_loop(matrix):

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j],end=" ")


matrix = [
    [1,2],
    [3,4],
    [5,6]
]


matrix_loop(matrix)