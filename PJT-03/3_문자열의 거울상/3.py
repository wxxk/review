import sys
sys.stdin = open('input.txt')
T = int(input())

for i in range(1, T+1):
    word = list(input())
    word.reverse()
    result = ''
    
    for i in range(len(word)):
        if word[i] == 'p':
            word[i]  == 'q'
        elif word[i] == 'q':
            word[i] == 'p'
        elif word[i] == 'b':
            word[i] == 'd'
        elif word[i] == 'd':
            word[i] == 'b'
        result= ''.join(word)
    print(result)