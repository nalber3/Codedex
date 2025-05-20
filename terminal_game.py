import random

#player chooses between three characters, each with its own weakness and strengths
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

#display of dictionaries showing stats

if character == 1:
    profile = {
            "attackspeed": 1,
            "hp": 60,
            "damage": 10,
            "experience": 0,
}

    print("You choose Warrior!")
elif character == 2:
    profile = {
            "attackspeed": 3,
            "hp": 38,
            "damage": 5,
            "experience": 0,
}

    print("You choose Archer!")
elif character == 3:
    profile = {
            "attackspeed": 2,
            "hp": 38,
            "damage": 20,
            "experience": 0,
}

    print("You choose Wizard!")


print(profile)

#some brief lore
print("Now defeat enough enemies to gain 20 xp in order to beat the game!\n"
      "Snakes are easier to fight and give small rewards,\n"
      "demons are the toughest, but their loot is big,\n"
      "orcs offer a moderated challange and decent outcomes\n"
      "...\n"
      "...\n"
      "...\n")



#Generates enemies until health = 0 or experience = 50, 
#gives the player the option to not engage in battle if not confident





while profile["experience"] < 50 and profile["hp"] > 0:


    enemy = random.randint(1, 3)

#Snake battle


    if enemy == 1:

        damageinflicted = 0

        battle = int(input("You found a snake!\n"
                           "Fight with the snake?, 1)yes / 2)no"))
        if battle == 1:
            

            while damageinflicted < 15:    

                #variance of damage
                damageratio = random.randint(1, 3)


             
                #Damage caused by the enemy
                snakeattack = random.randint(1,2)

                profile["hp"] -= snakeattack

                damageinflicted += (profile["attackspeed"] * profile["damage"])*(damageratio)

                #condition to kill the enemy
                if damageinflicted >= 15:
                    
                    #random generation of loot after killing the enemy
                    snakeloot = random.randint(1, 2)

                    if snakeloot == 1:
                        print(f"You killed the snake, lost {snakeattack} hp and found an apple, 5 hp recovered!\n"
                               "5 xp gained!")
                        profile["hp"] += 5
                        profile["experience"] += 5
                        #shows current stats, including xp and hp
                        print(profile)

                    elif snakeloot == 2:
                        print(f"You killed the snake and lost {snakeattack} hp!\n"
                               "5 xp gained!")
                        profile["experience"] += 5
                        print(profile)

        #goes back to the previous selection
        if battle == 2:
            print("Looking for more enemies ... ")        

    #condition to lose
    if profile["experience"] < 50 and profile["hp"] <= 0:
             
                print("You died! :'( \n"
                    "Try again")
                print(f"{snakeattack} Damage received")
    #condition to win
    elif profile["experience"] >= 50 and profile["hp"] > 0:
                print("Congratulations, you beat the game!")

        
  

#Orc battle
            
    elif enemy == 2:

        damageinflicted = 0        

        battle = int(input("You found an orc!\n"
                           "Fight with the orc?, 1)yes / 2)no"))
        if battle == 1:
            

            while damageinflicted < 30:

                #variance of damage
                damageratio = random.randint(1, 3)             

                orcattack = random.randint(2,4)

                profile["hp"] -= orcattack

                damageinflicted += (profile["attackspeed"] * profile["damage"])*(damageratio)
        
                if damageinflicted >= 30:

                    orcloot = random.randint(1, 3)

                    if orcloot == 1:
                        print(f"You killed the orc, lost {orcattack} hp and found two apples, 10 hp recovered!\n"
                               "10 xp gained!")
                        profile["hp"] += 10
                        profile["experience"] += 10
                        print(profile)

                    elif orcloot == 2:
                        print(f"You killed the orc, lost {orcattack} hp and found a strenght potion, 5 damage increased!\n"
                               "10 xp gained!")
                        profile["experience"] += 10
                        profile["damage"] += 5
                        print(profile)

                    elif orcloot == 3:
                        print(f"You killed the orc and lost {orcattack} hp!\n"
                               "10 xp gained!")
                        print(profile)
                    
        if battle == 2:
            print("Looking for more enemies ... ")

    if profile["experience"] < 50 and profile["hp"] <= 0:
             
                print("You died! :'( \n"
                    "Try again")
                print(f"{orcattack} Damage received")
    elif profile["experience"] >= 50 and profile["hp"] > 0:
                print("Congratulations, you beat the game!")


#Demon battle



    elif enemy == 3:

        damageinflicted = 0

        battle = int(input("You found a demon!\n"
                           "Fight with the demon?, 1)yes / 2)no"))
        if battle == 1:
            

            while damageinflicted < 40:
            
                #variance of damage
                damageratio = random.randint(1, 3)             

                demonattack = random.randint(10,30)

                profile["hp"] -= demonattack

                damageinflicted += (profile["attackspeed"] * profile["damage"])*(damageratio)
        
                if damageinflicted >= 40:

                    demonloot = random.randint(1, 3)

                    if demonloot == 1:
                        print(f"You killed the demon, lost {demonattack} hp and found a health potion, 20 hp recovered!\n"
                               "30 xp gained!")
                        profile["hp"] += 20
                        profile["experience"] += 30
                        print(profile)

                    elif demonloot == 2:
                        print(f"You killed the demon, lost {demonattack} hp and found two strenght potions, 10 damage increased!\n"
                               "30 xp gained!")
                        profile["experience"] += 30
                        profile["damage"] += 10
                        print(profile)

                    elif demonloot == 3:
                        print(f"You killed the demon, lost {demonattack} hp and found two apples and one strenght potion, 10 hp recovered and 5 damage increased!\n"
                               "30 xp gained!")
                        profile["experience"] += 30
                        profile["hp"] += 10
                        profile["damage"] += 5
                        print(profile)
        

        if battle == 2:
            print("Looking for more enemies ... ")

    if profile["experience"] < 50 and profile["hp"] <= 0:
             
                print("You died! :'( \n"
                    "Try again")
                print(f"{demonattack} Damage received")
    elif profile["experience"] >= 50 and profile["hp"] > 0:
                print("Congratulations, you beat the game!")