def mutliply(num1, num2):
    return sum(num1 for _ in range(num2)) if num1 > 0 and num2 > 0 else None
num1 = int(input("Enter the first positive number: "))
num2 = int(input("Enter the second positive number: "))
result = mutliply(num1, num2)
if result is not None:
    print(f"{num1} x {num2} = {result}")
