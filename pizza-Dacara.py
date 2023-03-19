control = ""
radius = 0
price = 0
print("Start = S, Quit = Q")
while True:
    control = input()
    if control == "S":
        print("Enter radius(In)")
        radius = float(input())
        area = 3.14159265359 * radius * radius
        print("Enter price")
        price = float(input())
        print("total price:")
        print(price / area)
    else:
        if control == "Q":
            print("Quit...")
            break
        else:
            print("Error: again input")