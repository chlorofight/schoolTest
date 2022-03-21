
def main():
    answer = input('do you wish to check core temp Y/N')
    if answer == 'y':
        print('checking core now....')
        print ('core normal')
    elif answer == 'n':
      print('Ok')
    else: print('did not answer')
    main()
main()
print('do you wish to Release nuclear reactor')
answer = input ('y/n')
if answer == 'y':
    print('Releaseing now')
elif answer =='n':
    print('release prevents explosions')
else: print('did not answer')

