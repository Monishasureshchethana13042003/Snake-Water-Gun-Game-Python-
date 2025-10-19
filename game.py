'''
snake=1
water=0
gun=-1

snake beats water
water beats gun
gun beats snake

'''
import random
import time

BOLD = "\033[1m"
END = "\033[0m"

def game(comp,user):
    win_conditions=[(0,1),(-1,0),(1,-1)]

    print("The result is ...", end="", flush=True)
    for _ in range(2):
        time.sleep(0.5)
        print(".", end="", flush=True)
    time.sleep(0.5)
    print()  # newline
    
    if(comp==user):
        print(BOLD + "\nits a tie!\n" + END)

    elif((comp,user) in win_conditions ):
        print(BOLD + "\nYou won! 🎉\n" + END)
    
    else:
        print(BOLD + "\nYOU LOST IT\n" + END)
    


dict={"s":1, "w": 0, "g":-1}

user_input=input("enter s for snake/ w for water/ g for gun: ")
user=dict.get(user_input)

comp_list=["s", "w", "g"]
comp_input= random.choice(comp_list)
comp= dict.get(comp_input)

# prints emojis
emoji_dict={"w":"💧", "s":"🐍", "g":"🔫"}

print(f"computer= {emoji_dict[comp_input]} and user= {emoji_dict[user_input]} ")
game(comp,user)
