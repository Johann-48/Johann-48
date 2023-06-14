from random import choice

print('**WELCOME TO ROCK PAPER AND SCISSOR GAME v0.1**')
c = input('Start(y) ')
rep = True
while rep == True:
    if c == 'y' or c == 'Y':
        r = 'Rock'
        p = 'Paper'
        s = 'Scissor'
        l = [r, p, s]
        o = choice(l)
        y = input('Press R for rock, P for paper, and S for scissor\n')
        if y == 'R' and o == r:
            print('Thats a tie')
        if y == 'R' and o == p:
            print('You lost')
        if y == 'R' and o == s:
            print('You won')
        if y == 'P' and o == r:
            print('You won')
        if y == 'P' and o == p:
            print('Thats a tie')
        if y == 'P' and o == s:
            print('You lost')
        if y == 'S' and o == r:
            print('You lost')
        if y == 'S' and o == p:
            print('You won')
        if y == 'S' and o == s:
            print('Thats a tie')
        qr = input('Repeat(R) or Not(N): ')
        if qr == 'R' or qr == 'r':
            rep = True
        elif qr == 'N' or qr == 'n':
            rep = False
