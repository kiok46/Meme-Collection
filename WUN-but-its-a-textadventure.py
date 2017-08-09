"""
We Are Number One but it is a Text Adventure written in Python

"""

def game_over():
    print("You are NOT Number One!!\n GAME OVER")
    exit()
    
print("\nWelcome to We are Number One! IMPORTANT: PUT YOUR ANSWERS IN QUOTATION MARKS!!!\n")
answer = input("Are you a real villian?\n| 'y' - Yes | 'n' - No | 'w' - Well technically... | : ")
if answer != 'w':
    game_over()
else:
    answer = input("\nHave you ever caught a good guy, like a real SUPERhero?\n| 'y' - Of course | 's' - Shake Head | 'n' - Nah Nah | : ")
if answer != 's':
    game_over()
else:
    answer = input("\nHAVE you ever tried a disguise??\n| 'y' - YES!! | 'n' - Nah Nah | : ")
if answer != 'n':
    game_over()
else:
    answer = input("\nAlright, I can see .. that I will have to TEAch you how to be villians.\n| 'f' - F*** you! | 's' - Screw you! | : ")
if answer != 's':
    print("Watch your language! This is a kids show. Wrong answer.")
    game_over()
else:
    print("A winner is you! You are truly number one. Congrats")
    exit()
