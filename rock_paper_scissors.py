import random

options = ["rock", "paper", "scissors"]
score_user = 0
score_computer = 0
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit ").lower()
    if user_input == 'q':
        break
    
    if user_input not in options:
        print("Invalid input")
        continue

    pick = random.randint(0,3)
    computer = options[pick]
    print("Computer picked: " + str(computer))
    if(computer == user_input):
        print("Tie")
    if computer == "rock" and user_input == "scissors":
        print("Computer wins!")
        score_computer += 1
    elif computer == "rock" and user_input == "paper":
        print("User wins!")
        score_user += 1
    elif computer == "paper" and user_input == "rock":
        print("Computer wins!")
        score_computer += 1
    elif computer == "paper" and user_input == "scissors":
        print("User wins!")
        score_user += 1
    elif computer == "scissors" and user_input == "paper":
        print("Computer wins!")
        score_computer += 1
    elif computer == "scissors" and user_input == "rock":
        print("User wins!")
        score_user += 1

print("Final score: ")
print("Computer wins = ", score_computer)
print("User wins = ", score_user)