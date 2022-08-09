import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(1, T+1):
    numbers = list(map(int, input().split()))
    odd = 0
    even = 0
    N = 0

    for j in range(0, len(numbers), 2):
        odd += numbers[j] * 2
    for k in range(1, len(numbers), 2):
        even += numbers[k]
   
    sum = odd + even
    
    if sum%10 == 0:
        print(f'#{i} {sum%10}')
    else:
        while sum%10 != 0:
            sum += 1
            N += 1
        print(f'#{i} {N}')
        