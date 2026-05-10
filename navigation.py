
def navigation_system(player, room):
    while True:
        print("Where would you go? ")
        print("1. Left")
        print("2. Right")
        choice = input(">")
        if choice == "1":
            room += 1
            break
        elif choice == "2":
            room -= 1
            break
    print(f"You are now in room {room}")
    if room == 10:
        print("You are now in BOSS level! Becareful!")
    return room
