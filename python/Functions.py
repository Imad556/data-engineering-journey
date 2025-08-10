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