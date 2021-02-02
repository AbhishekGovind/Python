num1 = float(input("Enter the first num: "))
opr = input("Enter the operator: ")
num2 = float(input("Enter the second num: "))

if opr == "+":
    print(num1 + num2)
elif opr == "-":
    print(num1 - num2)
elif opr == "/":
    print(num1 / num2)
elif opr == "*":
    print(num1 * num2)
else:
    print(" The operator is not valid ")