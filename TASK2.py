#               TASK 2
#      SIMPLE CALCULATOR IN PYTHON

#  ------------------------------------
# |        author: Avin Madhu          |
# |      Date  : 14 / 07 / 2024        |
#  ------------------------------------

import time

print("-------------------------------------------------------")
print("                     CALCULATOR                        ")
print("-------------------------------------------------------")
print("\n\n")
time.sleep(0.5)
print("what kind of operation do you want to do?\n")
time.sleep(0.5)
print("Enter the operation: \n")
print("1) Addition\n2) Subtraction\n3) Multiplication\n4) Division")
operation_choice = int(input("\nYour Choice: "))

# Variable to check wether to continue the program or stop
again = False

while(1):
    if operation_choice == 1:
        print("------------ADDITION------------\n\n")
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        time.sleep(0.2)
        print("\n",num1, " + ", num2, " = ", num1+num2) 
        break               
    elif operation_choice == 2:
        print("------------SUBTRACTION------------\n\n")
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        time.sleep(0.2)
        print("\n",num1, " - ", num2, " = ", num1-num2) 
        break    
    elif operation_choice == 3:
        print("------------MULTIPLICATION------------\n\n")
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        time.sleep(0.2)
        print("\n",num1, " X ", num2, " = ", num1*num2) 
        break    
    elif operation_choice == 4:
        print("------------DIVISION------------\n\n")
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        # checking division by zero
        if num2 == 0:
            print("\nCannot Divide by zero !")
            num2 = int(input("\nChoose another second number: "))
        time.sleep(0.2)
        print("\n",num1, " ÷ ", num2, " = ", num1/num2)
        break    
    else: 
        print("Inavlid Choice! choose again ")
        operation_choice = int(input("Yout Choice: "))

