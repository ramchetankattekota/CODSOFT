print("===== SIMPLE CALCULATOR =====")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose Operation")
print("+  Addition")
print("-  Subtraction")
print("*  Multiplication")
print("/  Division")

operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print("Result =", num1 + num2)

elif operation == "-":
    print("Result =", num1 - num2)

elif operation == "*":
    print("Result =", num1 * num2)

elif operation == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Cannot divide by zero!")

else:
    print("Invalid operation!")
