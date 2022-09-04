import sys
sys.stdin = open('2083.txt')

while True:
    name, age, we = input().split()
    age, we = int(age), int(we)
    if name == '#':
        break
    else:
        if age > 17 or we >= 80:
            print(name, 'Junior')
        else:
            print(name, 'Senior')