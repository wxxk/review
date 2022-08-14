# X의 각 자리가 등차수열을 ㅣ룬다면, 그 수는 한수
# 한 자리 자연수 => 한수
# 두 자리 자연수 => 한수
# 세 자리 자연수부터 => 등차수열인지 확인(각 자리수의 차이가 일정해야 등차수열)

import sys
sys.stdin = open('1065.txt')

N = int(input())
cnt = 0
for i in range(1, N+1):
    if len(str(i)) < 3:
        cnt += 1
    else:
        numbers = list(map(int, str(i)))
        if numbers[0] - numbers[1] == numbers[1] - numbers[2]:
            cnt += 1
        # print(numbers)
print(cnt)