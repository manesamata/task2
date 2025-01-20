def calculator():
    print("simple calculator")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
 
    choice = input("Enter your choice(1/2/3/4): ")
    
    num1 = float(input("enter first number:"))
    num2 = float(input("enter second number:"))
    
    if choice == '1':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif choice == '2':
        result = num1 - num2 
        print(f"{num1} - {num2} = {result}")
    elif choice == '3':
        result = num1 * num2 
        print(f"{num1} * {num2} = {result}")
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2 
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error! Division by zero not allowed.")
    else:
        print("Invalid choice.Please try again.")
calculator()