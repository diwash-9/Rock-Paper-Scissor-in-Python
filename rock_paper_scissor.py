import random

computer_wins = 0
user_wins = 0
draws = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type rock/paper/scissors or Q to quit.").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]

    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won.")
        user_wins += 1
    elif user_input == computer_pick:
        print("Draw")
        draws+= 1    
    else:
        print("Computer won.")
        computer_wins += 1
    continue

print("You won", user_wins, "times")
print("Computer won", computer_wins, "times")
print("Number of draws = ", draws)
print("Thank you")    
