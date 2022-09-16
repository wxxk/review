import sys
sys.stdin = open('4698.txt')

prime = []

check = [0] * (10**6+1)
for i in range(2, 10**6+1):
    if check[i] == 0:
        prime.append(i)

        for j in range(i, 10**6+1, i):
            check[j] =1

T = int(input())
for tc in range(1, T+1):
    D, A, B = map(int, input().split())
    result = 0

    for x in prime:
        if A <= x <= B and str(D) in str(x):
            result += 1
        if x > B:
            break
    print(f"#{tc} {result}")