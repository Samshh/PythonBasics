# Ceasar encryption
print("this ecryptor was made by sam")
plainText = input("Enter a word to enrypt: ")
distance = int(input("Enter the distance value: "))
code = ""
for ch in plainText:
    ordvalue = ord(ch)
    cipherValue = ordvalue + distance
    if cipherValue > ord("z"):
        cipherValue = ord("{") + distance -\
        (ord("z")- ordvalue + 1)
    code += chr(cipherValue)

print(code)
