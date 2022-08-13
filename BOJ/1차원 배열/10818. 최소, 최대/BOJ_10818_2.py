import sys
sys.stdin = open('10818.txt')

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

print(numbers[0], numbers[N-1])