game_start = "yes"

print("-" * 35)
print("A messengers journey")
print("-" * 35)
character_name = input("Please enter your character's name: ")
print("-" * 35)

while game_start == "yes":
    print(f"A messenger named {character_name} has been tasked to deliver an important message to the castle. \nAlong the way, {character_name} came to a crossroad. To the left, the path led through mountains. \nTo the right, the path led through a dark and scary forest. The mountains look safer, \nbut will probably take a few extra days to reach the castle. The scary forest would \nbe quicker, but it looks dangerous. \nDoes {character_name} go left or right?")
    print("-" * 35)
    answer_1 = input("[Enter: left or right] ")
    print("-" * 35)

    print("Travelling...")

    print("-" * 35)
    if answer_1 == "left":
        print(f"{character_name} decided that it would be safer to take the left path through the mountains. Along \nthe way, {character_name} came across a travelling merchant. Does {character_name} stop to see the merchants wares?")
        print("-" * 35)
        answer_2_a = input("[Enter: yes or no] ")
        print("-" * 35)
        if answer_2_a == "yes":
            print("Looking at merchants wares...")
            print("-" * 35)
            print("The merchant is actually a ninja and kills you")
            print("-" * 35)
            print("Game over")
        if answer_2_a == "no":
            print("You continue your journey. \nYou walk past a lake. Do you go fishing?")
            print("-" * 35)
            answer_3_a = input("[Enter: yes or no] ")
            print("-" * 35)
            if answer_3_a == "yes":
                print("You catch a fish and eat it. \nNow that you are well rested, you continue your journey. \nYou make it to the castle and delivered your message.")
                print("-" * 35)
                print("You win")
            if answer_3_a == "no":
                print("You starve to death")
                print("-" * 35)
                print("Game over")

    if answer_1 == "right":
        print("You come across a bridge. Do you cross the bridge?")
        bridge = input("[Enter: yes or no] ")
        print("-" * 35)
        while bridge == "no":
            print("There is no other way around. Do you cross the bridge?")
            bridge = input("[Enter: yes or no] ")
            print("-" * 35)
        print("You cross the bridge. It starts to fall apart. Do you make a run for it?")
        answer_2_b = input("[Enter: yes or no] ")
        print("-" * 35)
        if answer_2_b == "yes":
            print("You make it across just in time. \nYou walk into a troll. Do you attack it?")
            answer_3_b = input("[Enter: yes or no] ")
            print("-" * 35)
            if answer_3_b == "yes":
                print("You attack the troll and kill it. \nYou continue your journey and make it to the castle to deliver your message")
                print("-" * 35)
                print("You win")
            if answer_3_b == "no":
                print("You try to sneak around the troll, but it see's you and kills you")
                print("-" * 35)
                print("Game over")
        if answer_2_b == "no":
            print("You fall to your death")
            print("-" * 35)
            print("Game over")


    game_start = input("Play again: ")
    print("-" * 35)
