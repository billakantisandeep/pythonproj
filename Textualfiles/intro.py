message = 'Hello World'
msg = " I'm the only one"
print(message)
print(msg)

msg1 = """ This's will print the multiple lines of the string
which are now included in the double quotes """
print(msg1)
print(len(msg1))

print(msg[3])

print(message[0:5])
print(message[:5])
print(message[6:])

print(message.lower())
print(message.upper())
print(message.count('Hello'))
print(msg1.count('the'))
print(message.find('Sandeep'))
print(msg1.replace('the', 'sandeep'))
print(message.replace('World', 'Universe'))
print(message+' , '+msg)
message1 = '{}, {} . Welcome'.format(msg,message)