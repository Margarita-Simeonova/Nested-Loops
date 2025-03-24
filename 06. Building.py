floors = int(input())
rooms_per_floor = int(input())

for floor in range(floors, 0, -1):
    room_type = ''
    if floor == floors:
        room_type = 'L'
    elif floor % 2 == 0:
        room_type = 'O'
    else:
        room_type = 'A'

    for room in range(rooms_per_floor):
        print(f"{room_type}{floor}{room}", end=' ')
    print()  # New line after each floor
