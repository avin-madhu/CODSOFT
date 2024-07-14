#               TASK 2
#      PASSWORD GENERATOR IN PYTHON

#  ------------------------------------
# |        author: Avin Madhu          |
# |      Date  : 14 / 07 / 2024        |
#  ------------------------------------

import time
import random
print("-------------------------------------------------------")
print("                   PASSWORD GENERATOR                  ")
print("-------------------------------------------------------")
print("\n\n")
time.sleep(0.5)
password_length = int(input("Enter the Length of the pasword to generate: "))
print(" ----  Password Complexity  ---- ")
print("1) Basic\n2) Strong\n")
complexity = int(input("Your Choice: "))
character_set = "abcdefgheijklmnopqrstuvwxyz"
character_set_with_symbols = "abcdefgheijklmnopqrstuvwxyz1234567890@_!#$ "
password = ""

# To generate passwords that only contain alphabets
if complexity == 1:
    for i in range(password_length):
        length = len(character_set)
        random_index = random.randint(0,length)
        password += character_set[random_index]
    print("Your Password: ",password)

# To generate passwords that contains alphabets, numbers and special symbols 
elif complexity == 2:
    for i in range(password_length):
        length = len(character_set_with_symbols)
        random_index = random.randint(0,length)
        password += character_set_with_symbols[random_index]
    print("Your Password: ",password)
else:
    print("Invalid Input! Choose 1 or 2 and try again.")

    
    



