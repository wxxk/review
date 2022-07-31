import sys
sys.stdin = open ('input.txt')

T = int(input())    # 테스트 케이스 수

for i in range(1, T+1): # 테스트 케이스 수 만큼 반복
    num = int(input())
    score = list(map(int, input().split()))   #학생들의 성적
    score_list = [0] * 101    # 0점부터 100점까지 

    for j in score:
        score_list[j] += 1

    if score_list.count(max(score_list)) >= 2:
        score_list[score_list.index(max(score_list))] = 0
        print(f'#{i} {score_list.index(max(score_list))}')
    else:
        print(f'#{i} {score_list.index(max(score_list))}')