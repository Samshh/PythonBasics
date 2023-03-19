a = 0
b = 0
c = 0
control = ''
print('Start = S, Quit = Q')
while True:
    control = str(input())
    if control == "S":
        print('Enter first side:')
        a = int(input())
        print('Enter second side:')
        b = int(input())
        print('Enter third side')
        c = int(input())
        if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
            print('The triangle is a right triangle')
            print('Start = S, Quit = Q')
        else:
            print('The triangle is not a right triangle')
            print('Start = S, Quit = Q')
    else:
        if control == "Q":
            print('Quit...')
            break
        else:
            print('please enter either S or Q')
            