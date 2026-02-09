status = {"Power": 100, "Samples": 0}
inventory = []

while True:
    print("Enter mode\n1: Dig for Sample\n2: Report Status\n3: Emergency Stop")
    try:
        func = input()
        if func not in "123":
            raise ValueError
    except ValueError:
        print("Invalid input")
    else:
        match func:
            case "1":
                inventory.append(input("Enter sample name: "))
                status["Power"] -= 10
            case "2":
                print(status, inventory)
            case "3":
                break

command_batch = [
    "MOVE 10",
    "TURN LEFT",
    "MOVE 5",
    "MOVE five",    # Corrupted: 'five' is text, not a number
    "DIG",
    "MOVE 20",
    "XÆA-12",       # Corrupted: Unknown command
    "RETURN",
    "MOVE 15"
]

rover_state = {"x": 0, "y": 0, "samples": 0}

for command in command_batch:
    current = command.split()
    match current[0]:
        case "MOVE":
            try:
                rover_state["y"] += int(current[1])
            except ValueError:
                print("Error: Invalid distance ignored")
        case "DIG":
             rover_state["samples"] += 1
        case "TURN":
             print("Turning...")
        case _:
             print("Error: Unknown command sequence")
print(rover_state)
