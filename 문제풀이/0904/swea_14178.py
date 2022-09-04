import sys
sys.stdin = open('14178.txt')

T = int(input())

for tc in range(1, T+1):
    n, d = map(int,input().split())
    d=(d*2)+1

    result = n//d
    
    if (n%d) > 1:
        result+=1

    print(f'#{tc} {result}')
