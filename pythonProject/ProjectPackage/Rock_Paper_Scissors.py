from tkinter import *
import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors? : ").lower()  # input with uppercase

    if player == computer:
        print("Computer: ", computer)
        print("player: ", player)
        print("Draw! ")
    elif player == "rock":
        if computer == "paper":
            print("Computer: ", computer)
            print("player: ", player)
            print("YOU LOSE ! ")

        if computer == "scissors":
            print("Computer: ", computer)
            print("player: ", player)
            print("YOU WIN ! ")


    elif player == "scissors":
        if computer == "rock":
            print("Computer: ", computer)
            print("player: ", player)
            print("YOU LOSE ! ")

        if computer == "paper":
            print("Computer: ", computer)
            print("player: ", player)
            print("YOU WIN ! ")

    elif player == "paper":
        if computer == "scissors":
            print("Computer: ", computer)
            print("player: ", player)
            print("YOU LOSE ! ")

        if computer == "rock":
            print("Computer: ", computer)
            print("player: ", player)
            print("YOU WIN ! ")

    play_again = input("Play Again? (yes/no): ").lower()

    if play_again == "no":
        break

print("Thank you for playing! ")

window.mainloop()


