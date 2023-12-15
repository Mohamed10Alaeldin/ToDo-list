def opertion(num1, num2, choice):
    while choice:
        if choice == 1:
            return (num1 + num2)
        if choice == 2:
            return (num1 - num2)
        if choice == 3:
            return (num1 * num2)
        if choice == 4:
            return (num1 / num2)
        if choice == 5:
            return (num1 ** num2)
        else:
            choice = input("insert valid number please"
               "1- Addition (+)\n"
               "2- substraction (-)\n"
               "3- multiblication (*)\n"
               "4- division (/)\n"
               "5- power (^)\n"
               )
num1 = float(input("insert first number: "))
num2 = float(input("insert second number: "))
choice = input("choose the operation on these two numbers.\n"
               "1- Addition (+)\n"
               "2- substraction (-)\n"
               "3- multiblication (*)\n"
               "4- division (/)\n"
               "5- power (^)\n"
               )
print(opertion(num1,num2,int(choice)))

    