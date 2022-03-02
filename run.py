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
            print("The merchant is actually a ninja and kills you")
            print("Game over")
        if answer_2_a == "no":
            print("You continue your journey.")
            print("You walk past a lake. Do you go fishing?")
            answer_3_a = input("yes or no? ")
            if answer_3_a == "yes":
                print("You catch a fish and eat it")
                print("Now that you are well rested, you continue your journey")
                print("You make it to the castle and delivered your message")
                print("You win")
            if answer_3_a == "no":
                print("You starve to death")
                print("Game over")

    if answer_1 == "right":
        print("You come across a bridge. Do you cross the bridge?")
        bridge = input("yes or no? ")
        while bridge == "no":
            print("There is no other way around. Do you cross the bridge?")
            bridge = input("yes or no? ")
        print("You cross the bridge. It starts to fall apart. Do you make a run for it?")
        answer_2_b = input("yes or no? ")
        if answer_2_b == "yes":
            print("You make it across just in time")
            print("You walk into a troll. Do you attack it?")
            answer_3_b = input("yes or no? ")
            if answer_3_b == "yes":
                print("You attack the troll and kill it")
                print("You continue your journey and make it to the castle to deliver your message")
                print("You win")
            if answer_3_b == "no":
                print("You try to sneak around the troll, but it see's you and kills you")
                print("Game over")
        if answer_2_b == "no":
            print("You fall to your death")
            print("Game over") 


    game_start = input("Play again: ")
