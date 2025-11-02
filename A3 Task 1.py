# Define a function to calculate factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Take input from the user
num = int(input("Enter a number: "))

# Call the function and display the result
print("The factorial of", num, "is:", factorial(num))

