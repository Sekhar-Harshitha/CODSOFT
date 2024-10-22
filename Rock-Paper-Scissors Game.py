import random

options =("ROCK","PAPER","SCISSORS")
game=True
while game:
        player=None
        computer=random.choice(options)
        while True :
            player=int(input("--OPTIONS-- \n1.ROCK \n2.PAPER \n3.SCISSORS \n ENTER YOUR CHOICE:"))
            if player == 1:
                player_choice = options[0]
            elif player == 2:
                player_choice = options[1]
            elif player == 3:
                player_choice = options[2]
            else:
                player_choice = None

            if player_choice:
                print("PLAYER CHOICE:", player_choice)
                break
            else:
                print("INVALID INPUT")
        print("COMPUTER CHOICE:",computer)

        if player==computer:
            print("IT IS A TIE")
        elif player=="ROCK" and computer=="SCISSORS":
            print("YOU WIN!!")
        elif player=="SCISSORS" and computer=="PAPER":
            print("YOU WIN!!")
        elif player=="PAPER" and computer=="ROCK":
            print("YOU WIN!!")
        else:
            print("YOU LOSE!")
        while True:
            play_again = input("Play again? (Y/N):").strip().lower()
            if play_again in ['y', 'n']:
                play_again=="y"
                break
            else:
                print("ENTER VALID INPUT (Y/N):")
        if not play_again=="y":
            game=False
print("THANKS FOR PLAYING!!")