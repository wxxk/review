import sys
sys.stdin = open('1264.txt')

list_n = ['a', 'e', 'i', 'o', 'u']

while True:
    cnt = 0
    words = input().lower()
    if words == '#':
        break
    else:
        for word in words:
            if word in list_n:
                cnt+=1
    print(cnt)
    