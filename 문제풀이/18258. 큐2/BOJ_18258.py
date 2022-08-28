import sys
sys.stdin = open('18258.txt')
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    s = sys.stdin.readline().split()
    if s[0] == 'push':
        queue.append(s[1])
    elif s[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    elif s[0] == 'size':
        print(len(queue))
    elif s[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif s[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif s[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)