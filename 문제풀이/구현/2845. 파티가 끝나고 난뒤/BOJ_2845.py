import sys
sys.stdin = open('2845.txt')

L, P = map(int, input().split())
numbers = list(map(int, input().split()))
total = L * P

for number in numbers:
    print(number - total, end = ' ')