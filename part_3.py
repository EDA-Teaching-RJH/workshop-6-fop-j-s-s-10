try:
    speed = int(input("Enter Motor Speed: "))
    print("Speed set to", speed)
except ValueError:
    print("Error: Corrupted Signal. Maintaining current speed.")

def get_coordinate():
    while True:
        try:
            x = int(input("Enter x coordinate: "))
            if abs(x) > 100:
                print("Coordinate out of range")
                raise Error
        except:
            print("Invalid coordinate")
        else:
            break
    return x

get_coordinate()
