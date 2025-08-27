a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
op = input("Enter operator (+, -, *, /): ")


if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print("Error")
else:
    print("Error")
