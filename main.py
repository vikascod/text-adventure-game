name = input("enter your name: ")
print("welcome ", name, "to an adventure game :) ")

answer = input(
    "you are a wrong way.you want to find a right way you can go left or right.which way would you like to go? (left/right)")

if answer == "left":
    clue = input(
        "you reach to a river.you can walk to around and swim to arross.type walk to walk and swim to swim (walk/swim) ")

    if clue == "walk":
        print("you walk,You have to travel many miles then you lose the game.game Over")
    elif clue == "swim":
        print("you swim,You eaten by an elligeter.game Over")
    else:
        print("invalid option.you lose")

elif answer == "right":
    clue = input(
        "you reached to a bridge you want to cross or you want to go back (cross/back)")
    if clue == "cross":
        clue = input(
            "you cross the bridge you meet a old lady. do you talk to them (yes/no)")
        if clue == "yes":
            print("she give you a map to treasure then you become rich. you WIN")
        elif clue == "no":
            print("you LOSE the game")
        else:
            print("invalid option.you lose")
    elif clue == "back":
        print("you can go back then you reach on main road you get a car then you dicide to drive car and go home")
    else:
        print("invalid option.you lose")
else:
    print("invalid option.you lose")

print("thank for try this game", name)
