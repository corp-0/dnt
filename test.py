import dungeons
import os
calabozo = dungeons.default_dungeon.DefaultDungeon()

while True:
    os.system("cls")
    print(f"current room = {calabozo.current_room}")
    print()
    print("Visited rooms:")
    for i in range(len(calabozo.rooms)):
        print(f"{calabozo.rooms[i]}")
    print()
    print("Doors:")
    for i in range(len(calabozo.current_room.doors)):
        print(f"{i}. {calabozo.current_room.doors[i].direction.name}")

    choice = int(input("Where to?\n> "))
    calabozo.move_to(calabozo.current_room.doors[choice])