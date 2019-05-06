ab = {
    'sandeep': 'sandeep@gmail.com',
    'Larry': 'larry@perl.com',
    'matsumoto': 'matsumoto@ruby.com',
    'page': 'page@google.com'
}

print("sandeep's address is ", ab['sandeep'])

#Delete a key-value pair 
del ab['page']

print('\n There are {} contacts in the address book\n', format(len(ab)))

for name,address in ab.items():
    print('Contact {} at {}'.format(name,address))

#Adding a key-value pair 
ab['guido'] = 'guido@python.org'

if 'guido' in ab:
    print("\n Guido address is", ab['guido'])


