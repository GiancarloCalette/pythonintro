def print_menu():
    separator = "======================"
    print(separator)
    print("Calc 5000")
    print(separator)
    print("[1] Sum two numbers")
    print("[2] Substract two numbers")
    print("[3] Multiply two numbers")
    print("[4] Divide two numbers")

print_menu()
opt = input("Please select an option: ")
print(opt)

if opt == "1":
   num1 = float(input("Type a the first number: "))
   num2 = float(input("Type a the second number: "))
   result = num1 + num2
   print(result)
elif opt == "2":
    num1 = float(input("Type a the first number: "))
    num2 = float(input("Type a the second number: "))
    result = num1 - num2
    print(result)
elif opt == "3":
    num1 = float(input("Type a the first number: "))
    num2 = float(input("Type a the second number: "))
    result = num1 * num2
    print(result)
elif opt == "4":
    num1 = float(input("Type a the first number: "))
    num2 = float(input("Type a the second number: "))
    if num2 == 0:
        print("We cant divide by 0")
    result = num1 / num2
    print(result)