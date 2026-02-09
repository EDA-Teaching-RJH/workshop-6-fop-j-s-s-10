sample_bay = ["Basalt", "Silica", "Iron", "Dust"]
print(sample_bay[0])
print(sample_bay[-1])
print(len(sample_bay))

for sample in sample_bay:
    print(f"Transmitting data for: {sample}")

new_findings = []
i = 3
while i:
    i -= 1
    new_findings.append(input("Enter rock type: "))
print(new_findings)

if "Dust" in sample_bay:
    sample_bay.remove("Dust")
print(sample_bay)
