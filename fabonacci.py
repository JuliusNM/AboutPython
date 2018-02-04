# Function for nth Fibonacci number
def Fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

# Driver Program

print(Fibonacci(5))

#Another approach to print the fibonacci numbers


def fib():
    a, b = 0, 1
    while True:            # First iteration:
        yield a            # yield 0 to start with and then
        a, b = b, a + b
#Implimentation
print(next(fib()))
for index, fibonacci_number in enumerate(fib()):
    print('{i:4}:{f:3}'.format(i=index, f=fibonacci_number))
    if index == 10:
        break
