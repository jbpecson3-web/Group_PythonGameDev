import attack_system, random, monsters_intents, textstuff
import inventory_system
from monsters import spawn_monster

menu = ["1. Attack", "2. Defend", "3. Skill", "4. Inventory"]

def display_menu():
    for menu_item in menu:
        print(menu_item)

def battleloop(player):
    player_name = player["name"]
    player_hp = player["hp"]
    player_atk = player["atk"]
    player_def = player["def"]
    extra = 0
    tired = False
    pattern = 0

    monst_name, monst_atk, monst_hp, monst_def = spawn_monster() #12
    textstuff.spawn(player_name, monst_name)

    while True:
        viewed_inventory = False
        #CHECKER
        if tired: #if the monster is tired
            textstuff.tired(monst_name) #skips everything
            pattern = 0
        else:
            if pattern != 99: # 99 means viewed inventory
                pattern = random.randrange(1, 3) #pick a num 1-3, never plays if tired
                monsters_intents.patpat(monst_name, pattern, monst_atk) #this monster intent
        
        #DECISION
        display_menu()
        action = int(input("Action\n>"))

        #PLAYER ATTACK
        print(f"---------PLAYER TURN----------")
        if action == 1:
            monst_hp = attack_system.damage_monster(player_name, monst_hp, player_atk, monst_def, extra) #5
        
            #is monster dead?
            if monst_hp <= 0:
                print(f"---------PLAYER TURN----------")
                textstuff.defeat(player_name, monst_name)
                return player_hp #so it won't return the monster's health as the player's

            print(f"The {monst_name} has {monst_hp} hp remaining")
        #TO BE ADDED (SKILLS)
        elif action == 2:
            pass
        elif action == 3:
            pass
        elif action == 4:
            inventory_system.display_inventory(player)
            pattern = 99
            continue
        else:
            print("invalid")
            pass
        
        print(f"---------PLAYER TURN----------")

        #MONSTER ACTION
        if tired == True:
            textstuff.rest(monst_name)
            tired = False
        else:
            if pattern == 1:
                print(f"---------MONSTER TURN---------")
                player_hp = monsters_intents.helit(monst_name, player_hp, monst_atk, player_def) #wow, didn't think this would work
            elif pattern == 2:
                print(f"---------MONSTER TURN---------")
                player_hp = monsters_intents.hehit(monst_name, player_hp, monst_atk, player_def)
                tired = True #be tired
            else:
                print(f"something broke idiot!")
            
        #r u ded?
        if player_hp <= 0:
            break
        
        print(f"{player_name}'s HP Remaining: {player_hp}") #eases on if statements
        print(f"---------MONSTER TURN---------")

    return player_hp