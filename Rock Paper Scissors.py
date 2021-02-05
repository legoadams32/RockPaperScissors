import random
import time
exit = False
print("Welcome to the rock paper scissors")
time.sleep(2)
print("The objective is to beat the computer at the rock paper scissors")
time.sleep(3)

while(exit == False):

    print("Do you choice rock paper or scissors")
    user_input = input("What is your choice: ")

    if user_input == ("rock" or "Rock"):
        user_choice = 1
    elif user_input == ("scissors" or "Sicissors"):
        user_choice = 2
    elif user_input == ("paper" or "Paper"):
        user_choice = 3
    else:
        print("There was a error Exiting program")
        break

    computer_choice = random.randint(1,3) #generates the computers answer

    if user_choice == computer_choice:
        if user_choice == 1:
            print("It was a tie you both picked rock")
        elif user_choice == 2:
            print("It was a tie you both picked scissors")
        elif user_choice == 3:
            print("It was tie you both picked paper")
        else:
            print("Error")
    
    elif user_choice == 1 and computer_choice == 2:
        print("You won with rock computer picked scissors")
    
    elif user_choice == 1 and computer_choice == 3:
        print("You lost the computer picked paper")
    
    elif user_choice == 2 and computer_choice == 1:
        print("You lost the comupter picked rock")
    
    elif user_choice == 2 and computer_choice == 3:
        print("You won with scissors computer picked paper")
    
    elif user_choice == 3 and computer_choice == 1:
        print("You won with paper the computer picked rock")

    elif user_choice == 3 and computer_choice == 2:
        print("You lost the computer picked sisscors")
    
    else:
        print("There was a error")
        break

    time.sleep(2)
    user_continue = input("Would you like to keep playing yes or no: ")

    if user_continue == "no":
        print("Exiting")
        break