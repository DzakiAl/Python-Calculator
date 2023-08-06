print("Hello Welcome to Python Calculator")
print("Please enter which calcullation did you want")
print("1. Increment operation")
print("2. Decrement operation")
print("3. Multiplication operation")
print("4. divide operation")

choice = int(input("Enter your choice: "))

if choice == 1 :
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter second number: "))
    increment_result = first_number + second_number
    print(increment_result)
elif choice == 2:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    decrement_result = first_number - second_number
    print(decrement_result)
elif choice == 3 :
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    multiplication_result = first_number * second_number
    print(multiplication_result)
elif choice == 4 :
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    divide_result = first_number / second_number
    print(divide_result)
else :
    print("Please enter right number")