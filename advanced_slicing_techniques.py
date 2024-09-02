# Task 1: 

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 103, 104, 105, 106]
second_week_temperatures = temperatures[7:14]
print(f"Temperatures for the second week: {second_week_temperatures}")


# Task 2:

over_100 = []
for temp in temperatures:
    if temp > 100:
        over_100.append(temp)
    else:
        continue
print(f"Temperatures over 100 degrees: {over_100}")