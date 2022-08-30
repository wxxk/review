from pprint import pprint
import sys
sys.stdin = open('2606.txt')\

def dfs(i):
    stack = [i]
    visited[i] = True

    while stack:
        cur = stack.pop()
        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

dfs(1)
print(sum(visited)-1)