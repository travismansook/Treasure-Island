print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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

quest_one = input("You are in the desert. You find a pyramid, do you want to go inside or climb it?\nType 'climb' to climb the pyramid or Type 'inside' to head on inside!\n")
if(quest_one == "inside"):
    quest_two = int(input("You made it inside the pyramid. There are several rooms do you want to enter room '1', '2', or '3'\n"))
    if quest_two == 1:
        print("SURPRISE! You have awoken the mummies and they attacked you.\nGame Over!")
    elif quest_two == 2:
        print("You walked into the room filled with darkness. All of a sudden...BAM! The door abruptly slammed shut behind you locking you in the dark room with no escape.\nGame Over!")
    else:
        quest_three = input("You walked inside the room and see water all around but see something across. Do you want to 'swim' across or use the 'boat' lying in the corner?\n")
        if quest_three == "swim":
            print("You started swimming across. Getting closer and closer, you see the light! As you began to reach the end, something grabs you!\nGame Over!")
        elif quest_three == "boat":
            print("You got into the boat and successfully made it across and made it to the light!\nYou Win!")
else:
    print("You began to climb the pyramid. You were making good progress. Taking your step after step until...YOU SLIPPED AND FELL. GG\nGame Over!")