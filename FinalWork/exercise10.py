
def print_zero_counter(matrix):
    zero_counter = 0
    for row in matrix:
        for el in row:
            if el == 0:
             zero_counter = zero_counter + 1
    return zero_counter



matrix = [

    [0 ,1 ,1],
    [0 ,1 ,0],
    [1 ,0 ,0]
]
print("Summer of zeros in this matrix: ", print_zero_counter(matrix))