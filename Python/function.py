#함수와 람다 표현식

#함수 - 특정한 작업을 하나의 단위로 묶어 놓은 것, 불필요한 소스코드의 반복을 줄일 수 있음
#내장 함수: 파이썬이 기본적으로 제공하는 함수
#사용자 정의 함수: 개발자가 직접 정의하여 사용할 수 있는 함수
"""
def 함수명(매개변수):
  실행할 소스코드
  return 반환 값
"""
def add(a, b):
  return a + b

print(add(b=3, a=7))  #파라미터의 변수 직접 지정 가능(순서 상관 없이)

a = 0

def func():
  global a  #global 키워드로 변수를 지정하면 해당 함수에서 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조
  a += 1
  b = a
  
  return a, b #파이썬에서 함수는 여러 개의 반환 값을 가질 수 있음

#람다 표현식 - 특정한 기능을 수행하는 함수를 한 줄로 작성할 수 있음
print((lambda a, b: a + b)(3, 7))

array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
  return x[1]

print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))  #람다 표현식으로 간단하게 표현 (키 함수는 보통 일회용이기 때문에 적합)

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result = map(lambda a, b: a + b, list1, list2)  #여러 개의 리스트에 람다 표현식으로 함수 적용
