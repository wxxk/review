import sys
sys.stdin = open('3003.txt')

chess = [1, 1, 2, 2, 2, 8]
N = list(map(int, input().split()))

for i in range(len(chess)):
    print(chess[i]-N[i], end = ' ')
