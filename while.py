number = 23 
running = True 

while running:
    guess = int(input('Enter the integer:'))

    if guess == number:
        print('congrats')
        running = False

    elif guess > number:
        print ('you had guessed a higher no.')

    else: 
        print('Guess bit lesser no.')
    
else:
    print('The while loop is over')

print('Done')