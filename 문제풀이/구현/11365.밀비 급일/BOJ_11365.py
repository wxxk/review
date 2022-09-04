import sys
sys.stdin = open('11365.txt')

while True:
    word = input()
    len_word = len(word)
    if word == 'END':
        break
    else:
        print(word[-1::-1])