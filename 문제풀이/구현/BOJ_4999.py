import sys
sys.stdin = open('4999.txt')

me = input()
hos = input()

if len(me) >= len(hos):
    print('go')
else:
    print('no')