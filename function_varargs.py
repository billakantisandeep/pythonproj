def total(a=5, *numbers, **phonebook):
    print('a', a)

    #Iterate through all the items in a tuple.

    for single_item in numbers:
        print('Single item', single_item)

    #Iterate through all the items in the dict 

    for first_part,second_part in phonebook.items():
        print(first_part,second_part)

total(10,1,2,3,Jack=123,John=234,Inge=2344)

