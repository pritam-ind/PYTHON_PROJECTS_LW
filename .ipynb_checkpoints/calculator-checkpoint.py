while True:
    operation = ["+", "-", "*", "/"]
    
    op = input("Enter the operation or 'exit' to stop:").strip()

    if op == "exit":
        print("Byy Byy Sir, Please visit again!")
        break
    elif op not in operation:
        print("\n!!!Enter a valid operation!!!\n")

    else:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
    
        # if op=="exit":
        #     break
    
        if op=="+":
            print(f"\n[Sum of {num1} and {num2} is {num1+num2} ]")
    
        elif op=="-":
            print(f"\n[Difference of {num1} and {num2} is {num1-num2} ]")
    
        elif op=="*":
            print(f"\n[Multiplication of {num1} and {num2} is {num1*num2} ]")
    
        elif op=="/":
            if num2 != 0:
                print(f"\n[Division of {num1} and {num2} is  {num1+num2}]")
            else:
                print("Error: Zero division not allowed!")
        print()