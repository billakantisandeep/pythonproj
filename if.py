number = 23 
guess = int(input('Enter the number:'))

if guess == number:
    print('congrts you had guess it right')
    print( 'You wont win any prizes for this')

elif guess < number:
    print('your guess is lower than the number')
    print(' Guess more than the no. you had mentioned')

else:
    print(' your guess is higher than the no.')

print('Done')
