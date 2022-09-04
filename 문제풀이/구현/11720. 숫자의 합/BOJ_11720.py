import sys
sys.stdin = open('11720.txt')

n = int(input())
numbers = list(map(int,input()))
total = 0

print(sum(numbers))
