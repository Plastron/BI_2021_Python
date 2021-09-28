#a simple calculator

while True:
    num1 = int(input("Enter first number: "))
    operation = str(input("Enter operation: "))
    num2 = int(input("Enter second number: "))

    if operation == '+':
        print(num1 + num2)

    elif operation == '-':
        print(num1 - num2)

    elif operation == '*':
        print(num1 * num2)

    elif operation == '/':
        print(num1 / num2)

        # check if user wants another calculation
        # break the while loop if answer is no
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
        break