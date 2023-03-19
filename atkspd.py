baseAtkSpd = 0
bonusAtkSpd = 0
level = 0
print("Enter base attack speed:")
baseAtkSpd = float(input())
print("Enter bonus attack speed %:")
bonusAtkSpd = float(input())
bonusAtkSpd2 = bonusAtkSpd / 100
print("Enter character level:")
level = float(input())
finalAtkSpd = baseAtkSpd * (1 + bonusAtkSpd2 * (level - 1))
print("Enter the base speed of the attack:", end='', flush=True)
print(baseAtkSpd)
print("Enter the bonus attack speed %:", end='', flush=True)
print(bonusAtkSpd)
print("Enter the level:", end='', flush=True)
print(level)
print("The character/s current attack speed is:", end='', flush=True)
print(round(finalAtkSpd,2))
