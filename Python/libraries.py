#자주 사용되는 표준 라이브러리



#내장 함수 - 기본적인 함수들을 제공
result = sum([1,2,3,4,5])
min_result = min(7,3,5,2)
max_result = max(7,3,5,2)
result = eval("(3+5)*7")  #문자열로 표현된 식의 결과값 반환
result = sorted([9,1,8,5,4], reverse=True)
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key=lambda x: x[1], reverse=True)



#itertools - 반복되는 형태의 데이터를 처리하기 위한 유용한 기능들을 제공(순열과 조합 라이브러리 등)
from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']

result = list(permutations(data, 3))  #순열
result = list(combinations(data, 2))  #조합
result = list(product(data, repeat=2))  #중복 순열
result = list(combinations_with_replacement(data, 2)) #중복 조합



#heapq - 힙 자료구조 제공, 우선순위 큐 기능을 구현하기 위해 사용



#bisect - 이진 탐색 기능 제공



#collections - 덱, 카운터 등의 유용한 자료구조 포함
from collenctions import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])  #반복가능한 객체가 주어졌을 때 내부의 원소가 몇 번씩 등장했는지 확인

print(counter['blue'])  #'blue' 개수 출력



#math - 필수적인 수학적 기능 제공(팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수 등)
import math

def lcm(a, b):  #최소 공배수(LCM)을 구하는 함수
  return a * b // math.gcd(a,b)



# time - time 라이브러리를 활용해 함수 수행시간 측정하기
import time
start_time = time.time()

#Coding...

end_time = tim.time()
print("time:", end_time - start_time)
