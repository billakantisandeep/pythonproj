names = [ 'sandeep', 'udvi', 'teju', 'minnu', 'john']

for index,name in enumerate(names, start=1):
    print(index,name)



#Lopping over the two lists at once:
names1 = [ 'sandeep', 'udvi', 'teju', 'minnu', 'john']
heros = ['spiderman', 'batman', 'ironman', 'thor', 'blackwidow']
universers = ['Marvel', 'DC', 'Marvel', 'Earth', 'Sun']

for index,name in enumerate(names1):
    hero = heros[index]
    print(f'{name} is actually {hero}')

#To make more intituative 

for name, hero, universe in zip(names1, heros, universers):
    print(f'{name} is actually {hero} from {universe}')

#Zip returns the tuple of values 
for value in zip(names1, heros, universers):
    print(value)

