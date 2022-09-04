from collections import deque
import sys
sys.stdin = open('5097.txt')

T = int(input())

for tc in range(1, T+1):
    n,m = map(int, input().split())
    numbers = deque(list(map(int, input().split())))
    cnt = 0

    while cnt < m:
        numbers.append(numbers.popleft())
        cnt += 1

    print(f'#{tc} {numbers[0]}')
