#               TASK 2
#     ROCK PAPER SCISSOR IN PYTHON

#  ------------------------------------
# |        author: Avin Madhu          |
# |      Date  : 14 / 07 / 2024        |
#  ------------------------------------

import time
import random
print("-------------------------------------------------------")
print("                 ROCK PAPER AND SCISSOR                ")
print("-------------------------------------------------------")
print("\n\n")
time.sleep(0.5)

print("------------------------  RULES  ----------------------")
print("-> Choose only from rock paper and scissor ")
print("-> If both computer and player shows the same choice it's a tie")
print("-> Rock beats scissor , Scissor beats Paper, Paper beats Rocks")
print("-> point is awarded to the player that shown the choice that beats the other ")
print("-> You can exit the game at beginning of any round")

user_choice= 0 # keep track of the choice the user takes
round = 1 # keeps track of the current round 
user_score = 0 # keeps track of the user score
computer_score = 0 # keeps track of the computer score

choice_dict = {1: "Rock", 2: "Paper", 3: "Scissor"}

name = input("\nEnter your player name: ")

while (1):
    print(f"------- ROUND {round} -----------")
    print("1) Rock : 1\n2) Paper: 2\n3) Scissor: 3")
    user_choice = int(input("\nEnter your choice: "))

    # incase the user chooses other than 1 2 or 3
    while (str(user_choice) not in "123"):
        user_choice = int(input("\nEnter a valid choice: "))

    if (user_choice == 1):
        computer_choice = random.randint(1,3)
        if (user_choice - computer_choice):
            print("\nIts's a tie")
            print(f" {name}: {user_score} || Computer: {computer_score}")
            print("\nWant to go for another round? (y/n): ")
            again = input()

            # if the user give somthing except y or n
            while(again != "y" or again != "n"):
                print("\nEnter a valid answer (y/n): ")
                again = input()
            if again == "y":
                round += 1
                continue
            else:
                break
        else:
            pass
            



