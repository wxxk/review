import sys
sys.stdin = open('6749.txt')

young = int(input())
mid = int(input())

gap = mid - young
mid += gap

print(mid)