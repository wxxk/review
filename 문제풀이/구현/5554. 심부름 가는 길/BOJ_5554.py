import sys
sys.stdin = open('5554.txt')

hour = 0
min = 0
for i in range(4):
    n = int(input())
    min += n
    if min//60 >= 1:
        hour += (min//60)
        min -= 60*(min//60)

print(hour)
print(min)