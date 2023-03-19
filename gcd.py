#gwapa si maam emmy
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("Enter the larger number: "))
b = int(input("Enter the smaller number: "))

print(f"the greatest common divisor is {gcd(a, b)}.")