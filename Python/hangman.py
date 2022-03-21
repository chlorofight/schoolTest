import random

words = ['gay', 'lit', 'leo']
to_win = 0

word = random.choice(words)

def main():
    global to_win, win, words, word
    win = len(word)
    lives = len(word) * 2
    print('your word is','_' * len(word), 'letters long')
    print('you start with', lives,' lives (length of word * 2)')


    while lives > 0:
        lives = len(word) * 2
        guess = input('take a guess \n')
        for i in guess:
            if i in word:
                print(i,'is in the word')
                to_win += 1
            if i not in word:
                print('sorry that is not in the word')
                lives -= 1
                print('you have', lives, 'lives left')
            if to_win == win:
                for_win = input('you have all the letters guess the word')
                if for_win == word:
                    print('you win would youl like to play again (y/n)')
                    agin = input().lower()
                    if agin == 'y':
                        main()
                    else:
                        exit()
                else:
                    again = input("""sorry you got the word wrong
would you like to play again""").lower()
                    if again == 'y':
                        main()
                    else:
                        exit()
main()
