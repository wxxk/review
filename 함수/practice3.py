# 두 숫자가 들어오면
# 합, 차, 곱, 나눗셈 결과
def my_com(x, y):
    ad = x + y
    sb = x - y
    mt = x * y
    
    if x != 0:
        dv = x / y
    else:
        dv = '불능'
    return(ad, sb, mt ,dv)

a, b = map(int, input().split())
print(my_com(a, b))