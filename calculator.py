import math 

print("Calculator Program || check calculatorLog.txt for output")
use = ""
while (use.lower != "n"):
    val1 = float(input("Enter first values : "))
    val2 = float(input("\n Enter second values : "))
    opp = input(
        "\n1. + \n2. - \n3. * \n4. / \n5. exponent(exp) \n Choose operator ::")
    eqn = ""
    if opp == "+":
        eqn = val1+val2
        print(eqn)
    elif opp == "-":
        eqn = val1-val2
        print(eqn)
    elif opp == "/":
        eqn = val1/val2
        print(eqn)
    elif opp == "*":
        eqn = val1*val2
        print(eqn)
    elif opp == "exp":
        eqn = pow(val1, val2)
        print(eqn)
    elif opp == "sqrt":
        eqn = pow(val1, val2)
        print(eqn)
    elif opp == "sin(a)":
        eqn = math.sin(a)
        print(eqn)
    
    else:
        print("!!! invalid operator entered !!!")
    use = input("Do you want to try again (y/n) : ")


Log_file = open("calculatorLog.txt", "a")
# print(Log_file.readable())
Log_file.write("\nEqn : {} {} {} = {} ".format(val1, opp, val2, eqn))
Log_file.close()
