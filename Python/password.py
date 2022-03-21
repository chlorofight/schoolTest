
import random
def main():
    cha = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!.,:)(&*^%$#'
    length = input('password length?')
    length = int(length)
    amount = input('how many')
    amount = int(amount)
    for p in range(amount):
        password = ''
        for c in range(length):
            password += random.choice(cha)
        print(password)
    yes = input('another')
    if yes == 'Yes':
         main()
    elif yes == 'yes':
         main()
    elif yes == 'y':
        main()
    elif yes == 'Y':
        main()
    else:
         end = input('do you wish to exit')
    if end == 'no':
             print('wow')
             main()
    elif end == 'n':
        main()
    else:
            exit()
main()

