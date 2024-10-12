#computer wouldn't run match statements#

con = input("Would you like to start? (y/n) ")

while con == "y":

    num1 = float(input("What's the first number? "))
    opp = input("What operation would you like to perform? ")
    num2 = float(input("What's the second number? "))

    if opp == "/" and num1 == "0" or num2 == "0":
        print("Error")
    else:
        if opp == "+":
            result = num1 + num2 
            print (f"{num1} + {num2} = {result}")
        elif opp == "-":
            result = num1 - num2
            print (f"{num1} - {num2} = {result}")
        elif opp == "*":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif num1 == "0" or num2 == "0":
            print("Error")
        elif opp == "/":
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        elif opp == "%":
            result = num1 % num2
            print(f"{num1} % {num2} = {result}")
        else:
            print("ERROR")
    
    q = input("Would you like to restart? (y/n) ")
    if q == "n":
        print("Quitting the apllication")
        break

    print("NEW EQUATION")






