game_start = "yes"

print("-" * 35)
print("A messengers journey")
print("-" * 35)
character_name = input("Please enter your character's name: ")
print("-" * 35)

while game_start == "yes":
    print(f"A messenger named {character_name} has been tasked to deliver an important message to the castle.")
    print(f"Along the way, {character_name} came to a crossroad. To the left, the path led through mountains.")
    print(f"To the right, the path led through a dark and scary forest.")
    print(f"The mountains look safer, but will probably take a few extra days to reach the castle.")
    print(f"The scary forest would be quicker, but it looks dangerous. Does {character_name} go left or right?")
    print("-" * 35)
    answer_1 = input("[Enter: left or right?] ")
    print("-" * 35)

    print("Travelling...")

    print("-" * 35)
    if answer_1 == "left":
        print("You come across a merchant. Do you stop and talk to the merchant?")
        answer_2_a = input("[Enter: left or right?] ")
        if answer_2_a == "yes":
            print("The merchant is actually a ninja and kills you")
            print("Game over")
        if answer_2_a == "no":
            print("You continue your journey.")
            print("You walk past a lake. Do you go fishing?")
            answer_3_a = input("[Enter: left or right?] ")
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
        bridge = input("[Enter: left or right?] ")
        while bridge == "no":
            print("There is no other way around. Do you cross the bridge?")
            bridge = input("[Enter: left or right?] ")
        print("You cross the bridge. It starts to fall apart. Do you make a run for it?")
        answer_2_b = input("[Enter: left or right?] ")
        if answer_2_b == "yes":
            print("You make it across just in time")
            print("You walk into a troll. Do you attack it?")
            answer_3_b = input("[Enter: left or right?] ")
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
