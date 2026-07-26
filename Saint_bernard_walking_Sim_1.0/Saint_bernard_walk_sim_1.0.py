print(r'''
              _
            ,/A\,
          .//`_`\\,
        ,//`____-`\\,
      ,//`[_ROVER_]`\\,
    ,//`=  ==  __-  _`\\,
   //|__=  __- == _  __|\\
   ` |  __ .-----.  _  | `
     | - _/       \-   |
     |__  | .-"-. | __=|
     |  _=|/)   (\|    |
     |-__ (/ a a \) -__|
jgs  |___ /`\_Y_/`\____|
          \)8===8(/

''')
print("Welcome to the saint bernard walking simulator.")
print("Your mission is to survive a walk with one of your Saint Bernards.")
dog =input(''' It is 6am on a cold winter morning. Your two dogs, Morty and Amos are waiting for you to choose which one of them will get to go on the walk today. Who do you choose? input [Morty] or [Amos] ''')
dog2 = 0
if dog == "Morty" or dog =="morty":
    dog = "Morty"
    dog2= "Amos"
elif dog == "Amos" or dog == "amos":
    dog = "Amos"
    dog2 = "Morty"
else:
    print("please pick a dog that is actually in your house")
choice1 = input(f" You decide to take {dog} for a walk today. You put on his leash, and leave the house. The snow is really coming down, and it is quite cold outside. "
                f"You walk down the driveway to the street. Do you go left? or Do you go right?  input: [left] or [right]")
if choice1 == "left" or choice1 == "LEFT":
    print (f" {dog} sees a deer out in the street and lunges forward! You try and let go of the leash, but your hand is caught! You are being pulled forward. {dog} rushes toward the deer dragging you behind, and "
           f"Directly into the path of speeding pickup truck! You did not survive the walk!  GAME OVER.")
elif choice1 == "right" or choice1 == "RIGHT":
    print(f" You and {dog} take a right and head up the hill.")
else:
    print("INVALID CHOICE! You hesitated to long in the cold. GAME OVER.")
choice2 = input(f"As you reach the top {dog} begins to get anxious and starts pulling you toward the side of the road. Do you go with {dog} or pull him back?   input: [GO] or [PULL]")
if choice2 == "GO" or choice2 == "go":
    print(f" You allow {dog} to drag you off the side of the road into the woods. It is clear something large has just recently gone down this path. {dog} pauses to sniff the ground. "
          f"All of a sudden his ears pull back, and he whips around to his left. "
          f"you spin yourself, trying to see what has got him so excited! But, Before you have the chance to react a large bear tackles you! You did not survive the walk!  GAME OVER ")
elif choice2 == "pull" or choice2 == "PULL":
    print(f"you pull {dog} back, No way you are going trekking through the woods in this weather. you and {dog} continue on your journey over the hill.")
else:
    print("INVALID CHOICE. you hesitated too long in the cold. GAME OVER")
choice3 = input(f"You and {dog} safely reach the turn around point and begin heading back towards home. You safely reach your driveway. do you take {dog}'s leash off and let him run? "
                f"End the walk by going into the house? or Take {dog2} for walk.  Input [LEASH] [HOUSE] [WALK]")
if choice3 == "LEASH" or choice3 == "leash":
    print(f" {dog} runs happily through the snowy yard. Congratulations! you have survived walking a Saint Bernard")
elif choice3 == "House" or choice3 == "HOUSE":
    print(f" You Take {dog} into the house {dog2} looks at you waiting for his turn to go on a walk. will you play again and take him? GAME OVER")
elif choice3 == "walk" or choice3 == "WALK":
    print(f"you decide to brake the elements again in order to take {dog2} for a walk, just a brave soul you are! PLEASE RESTART THE GAME.")
