import sys
sys.stdin = open('0.txt')

T = int(input())

for _ in range(T):
    num, m = map(int, input().split())
    num = list(map(int, str(num)))
    stack=[]

    for x in num:
        while stack and m > 0 and stack[-1] < x:
            stack.pop()
            m-=1
        stack.append(x)

    if m!=0:
        stack = stack[:-2]

    res=''.join(map(str, stack))
    # join은 str을 합쳐주기때문에
    # map을 이용해서 stack을 문자열로 변환
    print(res)