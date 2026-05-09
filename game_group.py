import battle, class_system, textstuff

#REQUIREMENTS
#1. dungeon game x
#2. player name add /
#3. stats /
#4. classes x
#5. ATTACK /
#6. defense and skill x
#7. inventory system x
#8. If die = end /
#9. game loop /
#10. menu /
#11. monster attacking /
#12. monster spawning /
#13. if kill boss = end x

#2
name = textstuff.naming()

player = { #3
    
    "name": name,
    "atk" : 5,
    "hp"  : 100,
    "def" : 5,
    "cls" : "THIS SHOULDN'T APPEAR",
    "inventory" : {
        "Health Potion": 2,
        "Shield": 1,    
        "Sword": 1
        }
}
    # displaying of the inventory
def display_inventory():
    print("Your Inventory:")
    if player ["inventory"]:
        for item_name, item_count in player["inventory"].items():
            print(f"> {item_name} x{item_count}")
    else :
        print ("Your inventory is Empty.")

    # add/use items
def add_item(item_name): 
    if item_name in player["inventory"]:
            player["inventory"][item_name] = player["inventory"][item_name] + 1
    else: 
        player["inventory"][item_name] = 1

def use_item(item_name):
    if item_name == "Health Potion":
        player["hp"] = player["hp"] + 25
    elif item_name == "Shield":
        player["def"] = player["def"] + 25
    elif item_name == "Sword":
        player["atk"] = player["atk"] + 25

    player["inventory"][item_name] = player["inventory"][item_name] - 1
    if player["inventory"][item_name] == 0:
        del player["inventory"][item_name]

def display_stat():
    print(f"{player["name"]} || ATK: {player["atk"]}\n Health: {player["hp"] } || Defense: {player["def"] }")

print(f"Welcome to the die, {player['name']}!")

player["cls"] = class_system.decide(player)
print(player["cls"])

#10
while player["hp"] > 0: #will this fix monster appear?
    #needs here:
    #random int does either battle room, treasure room, hallway (50% to do something), and boss room (only applicable after 10 rooms)

    #new problem: monster health becomes player health after death
    player["hp"] = battle.battleloop(player["name"], player["hp"], player["atk"], player["def"])

textstuff.ded(player["name"])