game_start = "yes"

while game_start == "yes":
    print("You come to a crossroad. Do you go left or right?")
    answer_1 = input("left or right? ")

    if answer_1 == "left":
        print("You come across a merchant. Do you stop and talk to the merchant?")
    else:
        print("You come across a bridge. Do you cross the bridge?")
        bridge = input("yes or no? ")
        while bridge == "no":
            print("There is no other way around. Do you cross the bridge?")
            bridge = input("yes or no?")
        print("You cross the bridge. It starts to fall apart. Do you make a run for it?")
    answer_2


    game_start = input("Play again: ")
