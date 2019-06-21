import hashlib
str = "sandeepbillakanti"
#Encoding sandeepbillaknti using encode() then sending to SHA256
result = hashlib.sha256(str.encode())
#Printing the equivalent hexadecimal value
print("The hexadecimal equivalent of SHA256 is : ")
print(result.hexdigest())

print("\r")

