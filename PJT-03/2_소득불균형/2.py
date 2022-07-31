
import sys
sys.stdin = open('input.txt')

T = int(input())                                # 전체 테스트 케이스 수

for i in range(1, T+1):
    N = int(input())                            # 사람수 N 명
    income = list(map(int, input().split()))    # 소득
    cnt = 0                                     # 평균 이하의 소득인 사람들의 수를 저장할 변수
    avg = sum(income) / N                       # 평균

    for j in income:                            # 소득을 돌면서
        if j <= avg:                            # 소득이 평균이하면
            cnt += 1                            # cnt에 1씩 더하기
    print(f'#{i} {cnt}')