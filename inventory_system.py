
    # displaying of the inventory
def display_inventory(player):
    while True:
        display_stat(player)
        print("Your Inventory:")
        if player ["inventory"]:
            for item_name, item_count in player["inventory"].items():
                print(f"> {item_name} x{item_count}")
        else :
            print ("Your inventory is Empty.")
        print ("1. Use Item")
        print ("2. Exit")
        choice = int(input(">"))
        if choice == 1:
            select_item(player)
        elif choice == 2:
            break


    #selecting item in inventory
def select_item(player):
    print("Your Inventory: \n")
    count = 1
    for item_name, item_count in player["inventory"].items():
        print(f"{count}. {item_name} x{item_count}")
        count = count + 1

    item_list = list(player["inventory"].keys())
    choice = int(input("What item would you use? \n"))
    use_item(player, item_list[choice - 1])


    # add/use items
def add_item(player, item_name): 
    if item_name in player["inventory"]:
            player["inventory"][item_name] = player["inventory"][item_name] + 1
    else: 
        player["inventory"][item_name] = 1

def use_item(player, item_name):
    if item_name == "Health Potion":
        player["hp"] = player["hp"] + 25
    elif item_name == "Shield":
        player["def"] = player["def"] + 25
    elif item_name == "Sword":
        player["atk"] = player["atk"] + 25

    player["inventory"][item_name] = player["inventory"][item_name] - 1
    if player["inventory"][item_name] == 0:
        del player["inventory"][item_name]

    #displays the current stat of the player
def display_stat(player):
    print(f"{player["name"]} || ATK: {player["atk"]}\nHealth: {player["hp"] } || Defense: {player["def"] }")