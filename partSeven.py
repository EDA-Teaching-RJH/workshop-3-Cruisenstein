con = input("Would you like to start? ")

while con == "yes":

    num1 = float(input("What's the first number? "))
    opp = input("What operation would you like to perform? ")
    num2 = float(input("What's the second number? "))

    if opp == "+":
        result = num1 + num2 
        print (f"{num1} + {num2} = {result}")
    elif opp == "-":
        result = num1 - num2
        print (f"{num1} - {num2} = {result}")
    elif opp == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif opp == "/":
        if num1 == "0" or num2 == "0":
             print("no")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    elif opp == "^":
        result = num1 ** num2
        print(f"{num1} ^ {num2} = {result}")
    elif opp == "%":
        result = num1 % num2
        print(f"{num1} % {num2} = {result}")
    elif opp == "quit" or num1 == "quit" or num2 == "quit":
        print("Quitting the apllication")
        break
    else:
        print("ERROR")
    print("NEW EQUATION")






