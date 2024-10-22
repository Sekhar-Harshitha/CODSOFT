import random

options =("ROCK","PAPER","SCISSORS")
player=None
computer=random.choice(options)

player=int(input("--OPTIONS-- \n1.ROCK \n2.PAPER \n3.SCISSORS \n ENTER YOUR CHOICE:"))
if player == 1:
    player_choice = options[0]  # ROCK
elif player == 2:
    player_choice = options[1]  # PAPER
elif player == 3:
    player_choice = options[2]  # SCISSORS
else:
    player_choice = None  # Invalid input

if player_choice:
    print("PLAYER CHOICE:", player_choice)
else:
    print("INVALID INPUT")
print("COMPUTER CHOICE:",computer)