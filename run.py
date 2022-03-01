game_start = "yes"

print("-" * 35)
print("A messengers journey")
print("-" * 35)
player_name = input("Please enter your name: ")
print("-" * 35)

while game_start == "yes":
    print(f"{player_name} comes to a crossroad. Do they go left or right?")
    answer_1 = input("left or right? ")

    print("Travelling...")

    if answer_1 == "left":
        print("You come across a merchant. Do you stop and talk to the merchant?")
        answer_2_a = input("yes or no? ")
        if answer_2_a == "yes":
            print("The merchant shows you his wares")
        else:
            print("You continue your journey")

    else:
        print("You come across a bridge. Do you cross the bridge?")
        bridge = input("yes or no? ")
        while bridge == "no":
            print("There is no other way around. Do you cross the bridge?")
            bridge = input("yes or no? ")
        print("You cross the bridge. It starts to fall apart. Do you make a run for it?")
        answer_2_b = input("yes or no? ")
        if answer_2_b == "yes":
            print("You make it across just in time")
        else:
            print("You fall to your death")
    


    game_start = input("Play again: ")
