import sys
sys.stdin = open('4101.txt')

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        if a > b :
            print('Yes')
        else:
            print('No')