import random as rd

running=True
while running:
    options=['rock','paper','scissors']
    player=None
    computer=rd.choice(options)
    while  player not in options:
        player=input("enter the choice(rock,paper,scissors): ")
    print(f"player: {player}" )
    print(f"computer: {computer}")
    if player ==computer:
        print("Tie Match ")
    elif player=='rock' and computer=='scissors':
        print("You Win")
    elif player=='paper' and computer=='scissors':
        print("You Win")
    elif player=='scissors' and computer=='paper':
        print("you win")
    else:
        print("you lose!")
    reset=input("play again(y/n): ")
    if reset.lower()=="n":
        running=False
print("Thanks for Playing")
        
