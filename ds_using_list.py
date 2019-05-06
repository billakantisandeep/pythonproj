#This is my shopping list 
shoplist = ['apples', 'banana', 'managoes']
print ('I have', len(shoplist), 'items to purchase')
print('the items are ', end = ' ')
for item in shoplist:
    print(item, end=' ')

print('\n I also have to buy rice')
shoplist.append('rice')
print('My shopping list  now', shoplist)

print('I will sort my list')
shoplist.sort()
print('The sorted shopping list is', shoplist)

print('The first item I should buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I brought the', olditem)
print('Myshoppoing list is ', shoplist)