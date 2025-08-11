#multiple arguments
def multiply(*args):
    result=1
    for num in args:
        result *= num
    return result

multiply_result = multiply(2, 3, 4)  # Example usage
print(f"Multiplication Result: {multiply_result}")



#MULTIPLE KEYWORD ARGUMENTS
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Example usage
print_info(name="Alice", age=30, city="New York")


#EXERCISE:

def fizz_buzz(n):
    for i in range (1,n+1):
        if i%3 ==0 :
            print("Fizz")

        elif i %5 ==0:
            print("Buzz")

        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        
        else:
            print(i)

fizz_buzz(15)  # Example usage



#ENUMERATE FUNCTION
groceries = ["milk", "bread", "eggs", "apples"]
for index, item in enumerate(groceries, start=1):
    print(f"{index}: {item}")


#another example of enumerate with multiple lists
students = ["Alice", "Bob", "Charlie", "David"]
marks = [85, 42, 77, 33]
for index, student,mark in enumerate(students,marks, start=1):
    if mark < 40:
        print(f"{index}. {student} has failed with a mark of {mark}.")
    else:
        print(f"{index}. {student} has passed with a mark of {mark}.")


#INCREASING PRICES BY PERCENTAGE
prices = [50, 75, 100, 200]
def increase_prices(prices, percentage):
    for i in range(len(prices)):
        prices[i] += prices[i] * (percentage / 100)
    return prices