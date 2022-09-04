import sys
# sys.stdin = open("input.txt")

n, k = map(int, input().split())
numbers = list(map(int, input().split()))
res=set()

for i in range(n-2):
    for j in range(i+1, n-1):
        for m in range(j+1, n):
            res.add(numbers[i]+numbers[j]+numbers[m])

res=sorted(list(res), reverse=True)
print(res[k-1])
