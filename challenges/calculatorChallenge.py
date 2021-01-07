#!/usr/bin/env python3

operators = ["+", "-", "*", "/"]
answer = None

while answer == None:
    firstNumber = input("Please enter your first number - ")
    secondNumber = input("Please enter your second number - ")
    operator = input("""What would you like to do?
                            To add, enter +
                            To subtract, enter -
                            To multiply, enter *
                            To divide, enter /""")
    try:
        firstNumber.isnumeric()
        secondNumber.isnumeric()
        if operator in operators:
            if operator == operators[0]:
                answer = int(firstNumber) + int(secondNumber)
            elif operator == operators[1]:
                answer = int(firstNumber) - int(secondNumber)
            elif operator == operators[2]:
                answer = int(firstNumber) * int(secondNumber)
            elif operator == operators[3]:
                answer = int(firstNumber) / int(secondNumber)
        print(f"{firstNumber} {operator} {secondNumber} = {answer}")

    except:
        if firstNumber.isnumeric() == False or secondNumber.isnumeric() == False:
            print("Please enter a VALID NUMBER")
        else:
            print("PLease enter a VALID OPERATOR")
        

