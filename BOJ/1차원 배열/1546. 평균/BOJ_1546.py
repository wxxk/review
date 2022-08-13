import sys
sys.stdin = open('1546.txt')

N = int(input())
numbers = list(map(int, input().split()))
max_num = 0
new_numbers = []
max_num = max(numbers)

for i in range(N):
    new_numbers.append((numbers[i]/max_num)*100)

print(sum(new_numbers)/N)