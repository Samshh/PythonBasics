#gwapa si maam emmy
numbers = []
while True:
    number = input("Enter a number or press Enter to quit: ")
    if number == "":
        break
    numbers.append(float(number))

sum = 0
for number in numbers:
    sum += number
average = sum / len(numbers)

print("The sum is", sum)
print("The average is", average)