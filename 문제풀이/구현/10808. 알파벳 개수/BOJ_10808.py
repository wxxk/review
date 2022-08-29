import sys
sys.stdin = open('10808.txt')

word = list(input())
list_n =[0]*26

for i in word:
    list_n[ord(i)-97] += 1

for j in range(len(list_n)):
    print(list_n[j], end= ' ')