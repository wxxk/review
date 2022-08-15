def func(x, y):
    x = 10
    y = 20
    print('함수안쪽 -->', x, y, a)

if __name__=='__main__':
    a = 100
    b = 200
    func(a, b)
    print('본체 -->', a, b)