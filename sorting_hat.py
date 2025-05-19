griffindor = 0
ravenclaw = 0
hufflepuff =0
slytherin = 0


#Question 1

answer = int(input("Do you like Dawn or Dusk?\n"
                   "1) Dawn\n"
                   "2) Dusk\n"   ))

if answer == 1:
  griffindor += 1
  ravenclaw += 1

elif answer == 2:
  hufflepuff += 1
  slytherin += 1

else:
  print("Wrong input.")

#Question 2

answer2 = int(input("When I'm dead, I want people to remember me as:\n"
                   "1) The Good\n"
                   "2) The Great\n"   
                   "3) The Wise\n"
                   "4) The Bold\n"))

if answer2 == 1:
  hufflepuff += 2

elif answer2 == 2:
  slytherin += 2

elif answer2 == 3:
  ravenclaw += 2

elif answer2 == 4:
  griffindor += 2

else:
  print("Wrong input.")

#Question 3

answer3 = int(input("Which kind of instrument most pleases your ear?\n"
                    "1) The violin\n"
                    "2) The trumpet\n"
                    "3) The piano\n"
                    "4) The drum\n"))

if answer3 == 1:
  slytherin += 4

elif answer3 == 2:
  hufflepuff += 4

elif answer3 == 3:
  ravenclaw += 4

elif answer3 == 4:
  griffindor += 4

else:
  print("Wrong input.")





houses = {
        "Griffindor": griffindor,
        "Ravenclaw": ravenclaw,
        "Hufflepuff": hufflepuff,
        "Slytherin": slytherin,

}





print(houses)

if griffindor >= 4:
  print("You go to Griffindor!")

elif ravenclaw >= 4:
  print("You go to Ravenclaw!")

elif hufflepuff >= 4:
  print("You go to Hufflepuff!")

else:
  print("You go to Slytherin!")