# Ceasar decryption
print("this decryptor was made by sam")
code = input("Enter code: ")
distance = int(input("Enter the distance value: "))
plainText = ""
for ch in code:
    ordvalue = ord(ch)
    cipherValue = ordvalue - distance
    if ch.isalpha():
        if cipherValue < ord("A"):
            cipherValue = ord("Z") - (distance - (ord("A") - ordvalue - 1))
    plainText += chr(cipherValue)

print(plainText)
