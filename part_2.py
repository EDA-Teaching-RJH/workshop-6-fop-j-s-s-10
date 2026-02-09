rover_status = {
    "Battery": 100,
    "Heater": "Off",
    "Camera": "Standby"
}

print(rover_status["Battery"])

rover_status["Battery"] = 85
rover_status["Heater"] = "On"
rover_status["Speed"] = 5
print(rover_status)

mission_log = [
    {"Site": "Crater A", "Radiation": "Low", "Water": False},
    {"Site": "Dune B", "Radiation": "High", "Water": True}
]
for i in mission_log:
    print(f"Site {i["Site"]} has {i["Radiation"]} radiation")
