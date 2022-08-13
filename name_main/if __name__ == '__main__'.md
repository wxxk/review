# `if __name__ == '__main__':`



```python
# hello.py
def hello(name):
    return f'hello~ {name}'
    
print(hello('batman'))
'''--------------------------------------------------------
>> hello~ batman'''
```

```python
# index.py
import main

print(hello.hello('superman')
'''--------------------------------------------------------
>> hello~ batman
>> hello~ superman'''
```

---------------------------------------------------------------------------------------------------------------------------------------

```python
# hello.py
def hello(name):
    return f'hello~ {name}'

if __name__ = '__main--':
	print(hello('batman'))
'''--------------------------------------------------------
>> hello~ batman
------------------------------------------------------------'''

# index.py
import main

print(hello.hello('superman')
'''--------------------------------------------------------
>> hello~ superman'''
```

- hello.py 에서 `print(__name__)` 을 하면 결과 >> `__main__`

- index.py 에서 `print(__name__)` 을 하면 결과 >> `__main__`

- index.py 에서 `print(hello.__name__)`을 하면 >> `hello`



-> 인터프리터에서 직접 실행했을 경우에만 if문 내의 코드를 돌리라는 명령!