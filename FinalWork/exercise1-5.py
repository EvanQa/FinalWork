#exercsie 1
#Write a for loop that prints the numbers from 12 to 24.

# for i in range(12,25):
#     print(i)
#exercise 2
#Write a for loop that prints the ODD numbers from 7 to 31

# for x in range(7, 31 + 1, 2):
#     print(x, end=" ")

#exercise 3
#Write a for loop that prints the EVEN numbers from 10 to-20.
# for i in range(10,20 + 1, 2):
#     print(i, end=" ")

#exercise 4
# Write a for loop that iterates through all numbers from 1 to 45. Print the following:
#● Foreach number that multiples of 3 print “Fizz”
#● Foreach number that multiples of 5 print “Buzz”
#● Foreach number that multiples of 3 and 5 print “FizzBuzz”

# for i in range(1, 46):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz ")
#     elif i % 3 == 0:
#         print("Fizz ")
#     elif i % 5 == 0:
#         print("Buzz ")
#     else:
#         print(i)

#exercise 5
#Write a function that receives an array as a parameter and calculates the sum
#of all the numbers in the given array (don’t use sum() function).


def calculate_sum_of_array(array):
    count = 0
    for numbers in array:
        count += numbers
        return count


numbers = [12, 42, 54, 25, 10]
result = calculate_sum_of_array(numbers)
print(result)