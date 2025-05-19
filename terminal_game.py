import random

character = int(input("Welcome to Lember, an RPG game of epic adventures!\n"
                      "...\n"
                      "...\n"
                      "...\n"
                      "...\n"
                      "...\n"
                      "Type a number to choose your character\n"
                      "...\n"
                      "1) Warrior (low attack speed, high health, medium damage)\n"
                      "...\n"
                      "2) Archer (high attack speed, medium health, low damage)\n"
                      "...\n"
                      "3) Wizard (medium attack speed, low health, high damage)\n"
                      "...\n"))


attackspeed = 0
hp = 0
damage = 0
experience = 0


if character == 1:
    profile = {
            "attackspeed": 1,
            "hp": 40,
            "damage": 10,
}

    print("You choose Warrior!")
elif character == 2:
    profile = {
            "attackspeed": 3,
            "hp": 25,
            "damage": 5,
}

    print("You choose Archer!")
elif character ==3:
    profile = {
            "attackspeed": 2,
            "hp": 15,
            "damage": 20,
}

    print("You choose Wizard!")


print(profile)

print("Now defeat enough enemies to gain 20 xp in order to beat the game!\n"
      "Snakes are easier to fight and give small rewards,\n"
      "demons are the toughest, but their loot is big,\n"
      "orcs offer a moderated challange and decent outcomes\n"
      "...\n"
      "...\n"
      "...\n")



#Generates enemies until maxhealth = 0 or experience = 10, 
#gives the player the option to not engage in battle





while experience < 100 and hp > 0:


    enemy = random.randint(1, 3)

#Snake battle


    if enemy == 1:

        damageinflicted = 0

        battle = int(input("You found a snake!\n"
                           "Fight with the snake?, 1)yes / 2)no"))
        if battle == 1:
            

            while damageinflicted < 20:    

                damageratio = random.randint(1, 3)


             

                snakeattack = random.randint(1,3)

                hp -= snakeattack

                damageinflicted += (attackspeed * damage)*(damageratio)
        
                if damageinflicted >= 20:

                    snakeloot = random.randint(1, 2)

                    if snakeloot == 1:
                        print(f"You killed the snake, lost {snakeattack} hp and found an apple, 5 hp recovered!\n"
                               "5 xp gained!")
                        hp += 5
                        experience += 5
                        print(profile)

                    elif snakeloot == 2:
                        print(f"You killed the snake and lost {snakeattack} hp!\n"
                               "5 xp gained!")
                        experience += 5
                        print(profile)
        if battle == 2:
            print("Looking for more enemies ... ")        


    if experience < 100 and hp <= 0:
             
                print("You died! :'( \n"
                    "Try again")
    elif experience >= 100 and hp > 0:
                print("Congratulations, you beat the game!")

        
  

#Orc battle
            
    elif enemy == 2:

        damageinflicted = 0        

        battle = int(input("You found an orc!\n"
                           "Fight with the orc?, 1)yes / 2)no"))
        if battle == 1:
            

            while damageinflicted < 40:            

                damageratio = random.randint(1, 3)             

                orcattack = random.randint(3,5)

                hp -= orcattack

                damageinflicted += (attackspeed * damage)*(damageratio)
        
                if damageinflicted >= 40:

                    orcloot = random.randint(1, 3)

                    if orcloot == 1:
                        print(f"You killed the orc, lost {orcattack} hp and found two apples, 10 hp recovered!\n"
                               "10 xp gained!")
                        hp += 10
                        experience += 10

                    elif orcloot == 2:
                        print(f"You killed the orc, lost {orcattack} hp and found a strenght potion, 5 damage increased!\n"
                               "10 xp gained!")
                        experience += 10
                        damage += 5

                    elif orcloot == 3:
                        print(f"You killed the orc and lost {orcattack} hp!\n"
                               "10 xp gained!")
                    
        if battle == 2:
            print("Looking for more enemies ... ")

    if experience < 100 and hp <= 0:
             
                print("You died! :'( \n"
                    "Try again")
    elif experience >= 100 and hp > 0:
                print("Congratulations, you beat the game!")


#Demon battle



    elif enemy == 3:

        damageinflicted = 0

        battle = int(input("You found a demon!\n"
                           "Fight with the demon?, 1)yes / 2)no"))
        if battle == 1:
            

            while damageinflicted < 20:
            

                damageratio = random.randint(1, 3)             

                demonattack = random.randint(15,50)

                hp -= demonattack

                damageinflicted += (attackspeed * damage)*(damageratio)
        
                if damageinflicted >= 50:

                    demonloot = random.randint(1, 3)

                    if demonloot == 1:
                        print(f"You killed the demon, lost {demonattack} hp and found a health potion, 20 hp recovered!\n"
                               "30 xp gained!")
                        hp += 20
                        experience += 30

                    elif demonloot == 2:
                        print(f"You killed the demon, lost {demonattack} hp and found two strenght potions, 10 damage increased!\n"
                               "30 xp gained!")
                        experience += 30
                        damage += 10

                    elif orcloot == 3:
                        print(f"You killed the demon, lost {demonattack} hp and found two apples and one strenght potion, 10 hp recovered and 5 damage increased!\n"
                               "30 xp gained!")
                        experience += 30
                        hp += 10
                        damage += 5
        

        if battle == 2:
            print("Looking for more enemies ... ")

    if experience < 100 and hp <= 0:
             
                print("You died! :'( \n"
                    "Try again")
    elif experience >= 100 and hp > 0:
                print("Congratulations, you beat the game!")