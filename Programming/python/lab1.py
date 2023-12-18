def check_numbers(num1, num2):
    if num1 == num2 or abs(num1 - num2) == 5 or num1 + num2 == 5:
        return True
    else:
        return False
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = check_numbers(num1, num2)
print(result)

---------------------
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("Enter a number: "))
result = factorial(n)
print("The factorial of", n, "is", result)
----------------------------------------
def print_primes(n):
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i, end=' ')
n = int(input("Enter a number: "))
print("Prime numbers from 0 to", n, "are:")
print_primes(n)
----------------------------------------
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))

if is_prime(n):
    print(n, "is prime")
else:
    print(n, "is not prime")
----------------------------------------

