def solve(a):
    return sum(a)

n = int(input())
numbers = []

for i in range(n):
    numbers.append(int(input()))

print(solve(numbers))