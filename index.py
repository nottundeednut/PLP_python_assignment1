Arg1 = int(input("Enter first number? "))
Arg2 = int(input("Enter second number? "))
Operator = input("Enter operator +, - , * or / ? ")

if Operator == '+':
    print("Result: ", Arg1 + Arg2)
elif Operator == '-':
    print("Result: ", Arg1 - Arg2)
elif Operator == '*':
    print("Result: ", Arg1 * Arg2)
elif Operator == '/' and Arg2 != 0:
    print("Result: ", Arg1 / Arg2)
elif Operator == '/' and Arg2 == 0:
    print("Error dividing by Zero")
else:
    print("Invalid Operator")