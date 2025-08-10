#PROBLEM 1
#SELECTING SECOND NUMBER OF THE LIST
def second_number(numbers):
    if len(numbers) < 2:
        return None
    return numbers[1]


#PROBLEM 2
#swapping the first and last elements of a list 
def swap_first_last(numbers):
    if len(numbers) < 2:
        return numbers
    numbers[0], numbers[-1] = numbers[-1], numbers[0]
    return numbers


#PROBLEM 3
def remove_duplicates(numbers):
    result = []
    for num in numbers:
        if num not in numbers:
            result.append(num)
    return result
#removing duplicates from a list
 

 #PROBLEM 4
 #SUM OF ALL EVEN#numbers in a list
def sum_of_even(numbers):
    return sum(num for num in numbers if num % 2 == 0)


#PROBLEM 5
#finding how many times a number appears in a list
def count_occurences(numbers, target):
    count = 0
    for num in numbers:
        if num == target:
            count += 1
    return count

#PROBLEM 6
#checking a list for palindrome
def is_palindrome(numbers):
    return numbers == numbers[::-1]
    

 #CREATING DEEPCOPY OF NESTED LISTS
import copy
nested_list = [[1, 2, 3], [4, 5, 6]]
deep_copy = copy.deepcopy(nested_list)

#DOUBLE THE MATRIX
matrix = [[1, 2, 3], [4, 5, 6]]
doubled_matrix = [[element * 2 for element in row] for row in matrix]

#FLATTENING A NESTED LIST
def flatten(nested_list):
    flat_list = []
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list


names= ["Alice", "Bob", "Charlie"]
A=[name for name in names if name.startswith('A')]

