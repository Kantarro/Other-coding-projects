# Trivial rock paper scissors game using dictionaries
import random

def main():
    
    # value of the key is it wins against
    gestures = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    while True:
        computer_choice = random.choice(["rock","paper","scissors"])

        player_choice = input("Choose a gesture: rock, paper, scissors ")

        if player_choice == gestures[computer_choice]:
            print("HA HA YOU LOSEEEEEE")
            print("I chose", computer_choice)

        elif computer_choice == gestures[player_choice]:
            print("NOOOO YOU WIN")
            print("I chose", computer_choice)

        else:
            print("WE TIED!")
            print("I chose", computer_choice)
    
main()