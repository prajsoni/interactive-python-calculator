while True:
    try: 
        Num_1 = int(input("Enter first number: "))
    except ValueError: 
        print("Please enter valid numbers")
        continue
    
    Sign = input("Enter an operator or exit: ")
    if Sign == "exit":
        break        
    elif Sign not in ["+", "-", "*", "/"]:
        print("Invalid operator")
        continue

    try:
        Num_2 = int(input("Enter second number: "))
    except ValueError: 
        print("Please enter valid numbers")
        continue

    if Sign == "/": 
        if Num_2 == 0:
            Result = "Cannot divide by zero"
        else:
            Result = Num_1 / Num_2

    elif Sign == "*":
        Result = Num_1 * Num_2

    elif Sign == "+": 
        Result = Num_1 + Num_2
    
    elif Sign == "-": 
        Result = Num_1 - Num_2
    
    
    print("Result:",  Result)



