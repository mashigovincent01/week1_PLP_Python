# Basic Calculator Program

print("This is a basic calculator app")
print("You must enter two numbers and an operator\n\n")

first_number = int(input("Enter First Number: "))
second_number = int(input("Enter Second Number: "))
operator = input("Enter operator e.g +, -, *, /: ")


if operator == "+":
    result = first_number + second_number
    print(f"{first_number} + {second_number} = {result}")
elif operator == "-":
    result = first_number - second_number
    print(f"{first_number} - {second_number} = {result}")
elif operator == "*":
    result = first_number * second_number
    print(f"{first_number} * {second_number} = {result}")
elif operator == "/":
    result = first_number / second_number
    print(f"{first_number} / {second_number} = {result}")
else:
    print("Invalid Operator!")