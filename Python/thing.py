import random
secret = random.randint(1,1000)
flag = True
while flag == True:
    guess = input('Your guess?:')
    guess = int(guess)
    if guess > secret:
        print('Too high')
        ans = abs(secret - guess)
        print(ans)
        if ans < 5:
            print('hot') 
    elif guess < secret:
        print('Too low')
    else:
        print('correct')
        OwO = input('Too play again type Yes:')
        if OwO in['yes','Yes',]:
                flag = True
        else:
             flag = False
