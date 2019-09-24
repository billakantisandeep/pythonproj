class Person():
    pass

person = Person()

#Dynamically setting the values for the attribute
person.first = "Sandeep"
person.last = "Billakanti"

print(person.first)
print(person.last)

first_key = 'first'
first_val = 'Sandeep'

setattr( person, first_key, first_val)
first = getattr(person, first_key)

print(first)