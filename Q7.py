# Q7. Calculate the factorial of a number using lambda function


factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

num = int(input("Enter a number: "))

print("Factorial of", num, "is", factorial(num))
