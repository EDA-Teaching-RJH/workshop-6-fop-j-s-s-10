travel_log = []

while True:
    try:
        slope_angle = int(input("Sensor Reading (Slope Angle): "))
    except ValueError:
        print("Sensor Glitch")
    else:
        if slope_angle > 45:
            print("CRITICAL TILT! HALTING.")
            break
        travel_log.append(slope_angle)
        print("Path Stable. Moving forward.")

print("Mission Terminated.")
print("Total steps taken:", len(travel_log))
print(travel_log)
