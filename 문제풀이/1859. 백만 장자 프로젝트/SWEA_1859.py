import sys
sys.stdin = open ('1859.txt')

T = int(input())

for i in range(1, T+1):
    n = int(input())
    list_n = list(map(int, input().split()))

    max_n = 0
