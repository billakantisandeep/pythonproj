while True:
    s = input('Enter something:')

    if s == 'quit':
        break
    if len(s) < 3:
        print('Enter something bigger string')
        continue
    print('Input is of sufficient lenght')

