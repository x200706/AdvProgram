def rotate(top, north, west, command):
    if command == "north":
        return 7 - north, top, west
    elif command == "south":
        return north, 7 - top, west
    elif command == "east":
        return west, north, 7 - top
    elif command == "west":
        return 7 - west, north, top
    return top, north, west

while True:
    I = int(input())
    if I == 0:
        break
    top, north, west = 1, 2, 3
    for _ in range(I):
        command = input()
        top, north, west = rotate(top, north, west, command)
    print(top)