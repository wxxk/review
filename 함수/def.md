# 함수

> 특정 기능을 루틴별로 작성해 놓은것

- 장점
  - 업무 단위의 모듈화를 통해 논리를 단순화
  - 재사용이 가능하므로 코드작성을 편하고 짧게 해줌
- 종류
  - 내장함수 : Print, input 등
  - 모듈함수 : 특정 모듈에 저장되어있음
  - 객체의 함수(메서드) : list객체에 append, sort 등
  - 사용자 정의함수 : 직접 만들어서 사용



### 함수 만들기

```python
def 함수명(인수들):
    처리할 문장들
    return 반환 값

'''
1. 함수명은 변수명 작성규칙과 동일
2. 사용문장보다 앞서서 만들어 질것
3. 함수내의 변수와 밖의 변수 혼동 주의
'''
```

- 예시 

```python
# 두 숫자를 전달받아 나눗셈 결과를 반환하는 함수
def division(x, y):
    if int(y) == 0:
        res == '불능'
    else:
        res = x / y
    return res

#  두개의 데이터를 전달받아 숫자 여부를 판별하는 함수
def end_check(x, y):
	if x.isnumeric() and y.isnumeric():
        return False
    else:
        return True
    
while True:
    a = input("\n 첫번째 숫자를 입력하세요...")
    b = input(" 두번째 숫자를 입력하세요...")
    
    if end_check(a, b):
        print("\n 프로그램을 종료합니다.")
        break
    k = division(a, b)
    print("{} 나누기 {}는 {} 입니다.".format(a, b, k))
```

- 문제 : 두 숫자가 들어오면 합, 차, 곱, 나눗셈 결과를 반환해주는 함수를 작성해라

  > 힌트 : return시 네 개 값을 패키징

```python
def my_com(x, y):
    ad = x + y
    sb = x - y
    mt = x * y
    
    if b != 0:
        dv = x / y
    else:
        dv = '불능'
        
	return(ad, sb, mt ,dv)
```



### 본체와 함수 간 데이터 흐름

```python 
def func(x, y):
    x = 10
    y = 20
    print('함수안쪽 -->', x, y, a)

if __name__=='__main__':
    a = 100
    b = 200
    func(a, b)
    print('본체 -->', a, b)
```



**주의 사항**

- 리스트 요소에 접근하면 값 변경이 가능



##### 인수의 기본 값 정의하기

```python
def find(source, ch, all= False):
    position=[]
    for i in range(len(source)):
        if source[i] == ch:
            position.append(i)
            if not all:break
	return position

s= '배구 우리나라 우생순 우승'

k = find(s, '우')
print(k)

k = find(s, '우', True)
print(k)
```



##### 키워드 인수

- 함수를 호출할 때 인수 이름을 통해 값을 전달

```python
def printing(source, repetition = 1):
    for i in range(repetition):
        print(source)
        
printing('korea')

printing(repetition = 5, source = "china")
```



##### 전역 변수 : 전역에서 통용되는 변수

```python
def change_state():
    global sw
    if sw:
        lbl['state'] = 'active'
    else:
        lbl['state'] = 'disabled'
    sw = not sw # 논리 부정을 시키고 탈출
    			# 값을 그대로 유지하고 있다가 다시 들어옴(재처리 가능)
```


리스트를 함수에 인수로 전달 시

```python
# 요소에 접근
def func(x):
    X[0] = 500
    
a = [10, 20, 30]
func(a)
# a[0] -> 500


------------------------------------------------
# 변수 자체로 접근
def func(x):
    x = [500, 600, 700]

a = [10, 20, 30]
func(a)
# a = [10, 20, 30]
```

