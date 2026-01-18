import random as rd
low=1
high=10
ans=rd.randint(low,high)
guess=0
is_run=True
print("python number  guessing  game")
print(f"select the number  between {low} to {high} " )
while is_run :
    gu=input("Enter the Guess :")
    if gu.isdigit():
        gu=int(gu)
        guess+=1
        if gu <low or gu>high:
            print("that number is out of range")
            print(f"please select the number  between {low} to {high} " )
        elif gu<ans:
            print("Too low Try Again!")
        elif gu>ans:
            print("Too high Try Again!")
        else:
            print(f"the correct ans {ans}")
            print(f"number of guess :{guess}")
            is_run=False
    else:
        print("INVALID GUESS")
        print(f"please select the number  between {low} to {high} " )
    
#print(ans)