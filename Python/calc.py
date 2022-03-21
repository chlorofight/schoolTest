import random
eq = '*/+-'
def main():
    number1 = input('first number or type random for a random number ')
    if number1 == 'random':
        number1 = random.randint(1,99999999999999)
        print('your number is:',number1)
    number2 = input('seccond number')
    if number2 == 'random':
        number2 = random.randint(1,99999999999999)
        print('your number is:',number2)
    number2 = int(number2)
    number1 = int(number1)
    equation = input('equation')
    if equation == 'random':
       se = random.choice(eq)
       print(se)
    if se == '+':
        print(number1 + number2)
        main()
    elif se == '-':
        print(number1 - number2)
        main()
    elif se == '*':
        print(number1 * number2)
        main()
    elif se == '/':
        print(number1 / number2)
        main()
    elif equation == '+':
        print(number1 + number2)
        main()
    elif equation == '*':
        print(number1 * number2)
        main()
    elif equation == '-':
        print(number1 - number2)
        main()
    elif equation == '/':
        print(number1 / number2)
        main()
    else:
        print('bruh why didnt you not answer with something')
        main()
main()
