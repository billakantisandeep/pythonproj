#I would recommand always using parantheses
#to indicate start and end of the tuple
#even though paranthesis are optional
#Explicit is always better than implict

zoo = ('python', 'elephant', 'tiger')
print('number of animals in the zoo are ', len(zoo))
new_zoo = 'monkey', 'lion', zoo  #Paranthesis is not required but good idea.
print('Number of cages in the new zoo are ', len(new_zoo))
print('all the animals in the new zoo are ', new_zoo)
print('Animals brought from the old zoo are ', new_zoo[2])
print('Last animal brought into the zoo is ', new_zoo[2][2])
print('no of animals in the zoo are',
        len(new_zoo)-1+len(new_zoo[2]))