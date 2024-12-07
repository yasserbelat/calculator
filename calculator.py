num1 = float(input("entre first number :"))
operation = input("entre a operation:")
num2 = float(input("entre second number :"))

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "**":
    print(num1 ** num2)
elif operation == "*":
    print(num1 * num2)
    print(num1 / num2)
elif operation == "/":
    if num2 == 0:
        print("Error: Dividing by 0 is not possible")
    else:
        print(num1 / num2)