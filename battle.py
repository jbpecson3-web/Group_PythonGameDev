import attack_system, random, monsters_intents, textstuff, skill_system, debuff, inventory
from monsters import spawn_monster

menu = ["1. Attack", "2. Defend", "3. Skill", "4. Rest","5. Inventory"]

def display_menu():
    for menu_item in menu:
        print(menu_item)

#resets stats to remove temporary boosts

#actual fight
def battleloop(player:dict):
    #game variables
    reset = player["atk"], player["def"] #saves default values
    extra = 0
    pattern = 0
    extra_mon = 0

    monster = spawn_monster() #12
    textstuff.spawn(player["name"], monster["name"])

    while True:
        #PRELIMINARY CHECKER
        player["def"] = reset[1] #sets to default values at the start of turn
        player["atk"] = reset[0]
        player["mp"]=skill_system.mp_add(player["mp"],player["mp_max"],1)

        if monster['tired'] == True: #if the monster is tired
            textstuff.tired(monster["name"]) #skips everything
            pattern = 0
        else: #otherwise, play monster intent
            pattern = monsters_intents.randomness(monster, pattern) #pick a num 1-3, never plays if tired

        monster['def'], monster['block'] = monsters_intents.heblock(monster, pattern)

        turn = True
        while turn == True:
        #PLAYER DECISION
            monsters_intents.patpat(monster, pattern) #this monster intent
            display_menu()
            debuff.which(player)
            action = input("Action\n>")

            #PLAYER ATTACK
            textstuff.player_turn()
            if action == "1": #attack
                monster['hp'] = attack_system.damage_monster(monster, player, extra) #5
                turn = False
                #TO BE ADDED (SKILLS)
            elif action == "2": #defend
                print(f"{player['name']} braced for impact... defense increased by 5 this turn!")
                player["def"] += 5 # Temporary defense boost
                turn = False
            elif action == "3": #skill
                player, extra = skill_system.skill_menu(player, monster, extra)
            elif action == "4": #rest
                skill_system.skill_rest(player)
                if player['poison'] > 1 or player['burned'] > 1:
                    player['poison'] = 0
                    player['burned'] = 0
                    print(f"{player['name']} also recovers from poison!")
                turn = False
            elif action == "5": #item
                player, extra = inventory.inven_menu(player, monster, extra)
            else: #if you're too lazy to act
                textstuff.nothing(player["name"])
                turn = False

        if monster['hp'] <= 0:
            textstuff.defeat(player["name"], monster['name'])
            print(f"--- BATTLE END ---")
            player = inventory.give_reward(player)
            break
        print(f"The {monster['name']} has {monster['hp']} hp remaining")
        textstuff.player_turn()

        #MONSTER ACTION
        if monster['tired'] == True:
            textstuff.rest(monster['name'])
            monster['tired'] = False
        else:
            monster, player = monsters_intents.monster_state(monster, player, pattern)

        #r u ded?
        if player["hp"] <= 0:
            break
        
        print(f"{player["name"]}'s HP Remaining: {player["hp"]}") #eases on if statements
        textstuff.monster_turn()

    return player["hp"]