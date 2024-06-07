# write 'hello world' to the console when the app is run
print('Hello, World!')


#I want you to create a rock,scissors,paper game with the following rules:

#Rock beats scissors
#Scissors beats paper
#Paper beats rock
#The game should be played between the user and the computer
#The user should be able to input their choice
#The computer should randomly select its choice
#The game should print the result of the game
#The game should be able to run multiple times
#The game should keep a running tally of the score
#The game should print the score after each round
#The game should ask the user if they want to play again after each round
#The game should print the final score when the user decides to stop playing
#the game must handle user inputs, putting them in lowercase and informing the user if they input an invalid choice

import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    score = {"user": 0, "computer": 0}

    while True:
        computer_choice = random.choice(choices)
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        print(f"Computer chose: {computer_choice}")
        print(f"You chose: {user_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
            score["user"] += 1
        else:
            print("Computer wins!")
            score["computer"] += 1

        print(f"Score: User - {score['user']}, Computer - {score['computer']}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print(f"Final Score: User - {score['user']}, Computer - {score['computer']}")

play_game()