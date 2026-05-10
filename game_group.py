import battle, class_system, textstuff
import navigation

#REQUIREMENTS
#1. dungeon game x
#2. player name add /
#3. stats /
#4. classes /
#5. ATTACK /
#6. defense and skill /
#7. inventory system x
#8. If die = end /
#9. game loop /
#10. menu /
#11. monster attacking /
#12. monster spawning /
#13. if kill boss = end x

#2
# name = textstuff.naming()

player = { #3
    
    "name": "name",
    "atk" : 100,
    "hp"  : 1000,
    "hp_max"  : 1000,
    "mp"  : 100,
    "mp_max"  : 100,
    "def" : 1,
    "cls" : "THIS SHOULDN'T APPEAR",

    #debuff counters
    "poison" : 0,
    "burned" : 0,

    "inventory": {
        "1": None,
        "2": None,
        "3": None
                }
}
if __name__ == "__main__":
    # player = class_system.decide(player)
    # input(">")

    # print(f"Welcome to the die, {player['name']}!")
    # input(">")

    #room navigation
    room = 0
# #10
    while player["hp"] > 0: #will this fix monster appear?
        #needs here:
        #random int does either battle room, treasure room, hallway (50% to do something), and boss room (only applicable after 10 rooms)
        room = navigation.navigation_system(player, room)
        player["hp"] = battle.battleloop(player)
    textstuff.ded(player["name"])
