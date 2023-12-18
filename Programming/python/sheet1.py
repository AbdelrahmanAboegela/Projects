def check_number():
    number = int(input("Enter a number between 0 and 100: "))
    print("The number is in the range of 0 and 100") if 0 <= number <= 100 else print("The number is outside the range of 0 and 100")
