level = 0
bonusAtkSpd = 0
baseAtkSpd = 0
print("Enter base atk spd")
baseAtkSpd = float(input())
print("Enter bonus atk spd %")
bonusAtkSpd = float(input())
bonusAtkSpd2 = bonusAtkSpd / 100
print("Enter character level")
level = float(input())
finalAtkSpd = baseAtkSpd * (1 + bonusAtkSpd2 * (level - 1))
print(round(finalAtkSpd,2))