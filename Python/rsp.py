#!/bin/python3
from random import randint
def main():

    player = input('rock(r), paper(p), or scissors(s)? ')
    print(player, 'vs ', end='')
    chosen = randint(1,3)
        #print(chosen)
    if chosen ==1:
            computer = 'r'
    elif chosen ==2:
            computer = 'p'
    else:
          computer = 's'
    print(computer)
    if player == computer:
        print('HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA DRAW')
    elif player == 's' and computer == 'p':
        print('wow u dont suck..... you win')
          
    elif player == 'p' and computer == 'r':
        print('wow u dont suck..... you win')
        Score = x + 1
    elif player == 's' and computer == 'r':
        print('wow u do suck..... you dont win')
    elif player == 'r' and computer == 'p':
        print('wow u do suck..... you dont win')
    elif player == 'r' and computer == 's':
        print('wow u dont suck..... you win')
    elif player == 'p' and computer == 's':
        print('wow u do suck..... you dont win')
    restart=input('Type yes to play again')
    if restart == 'yes':
        
            main()
    else:
                 exit()
main()

    
