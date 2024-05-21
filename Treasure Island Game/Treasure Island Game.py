print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

plane = input("""Your plane has an engine on fire. \nDo you stay with the plane and try to land or use the parachute and jump out? 
Type stay or jump
\n""")

if plane == "jump":
    river = input("""\nNice! \nYou jump out and your parachute snags in a tree. \nYou detach from your parachute and come to a river crossing. 
Do you cross the river or keep walking in the jungle and try go around? 
Type cross or go around\n\n""")

    if river == "go around":
        go_around = input("""\nAs you are walking you find an old abandoned town in the jungle. \nThere is a restaurant and near the restaurant there is a small boat. \nThere is also a small airport hangar with a helicopter and there appears to be an old jeep. \nDo you decide to take the helicopter, the boat, the jeep or stay at the restaurant?
Type helicopter, boat, jeep or restaurant\n\n""")
        if go_around == "helicopter":
            print("You start the helicopter and as the helicopter lifts off it explodes. Game Over.")
        elif go_around == "boat":
            print(
                "As your boat begins down the river it becomes apparent there is a leak. \nThe boat sinks. Game Over.")
        elif go_around == "jeep":
            print("The jeep runs out of gas and you are eaten by jungle animals. Game Over.")
        else:
            print("You Win!")
    else:
        print("As you start crossing the river a crocodile eats you. Game Over.")
else:
    print("Your plane explodes and you die. Game Over.")
