"""
거슬러 줘야하는 돈이 N원일 때,  *N은 10의 배수
거스름돈을 10원, 50원, 100원, 500원 짜리 동전으로 준다면
거슬러 주어야하는 동전의 최소개수를 구하시오
"""

import sys

n = int(sys.stdin.readline().rstrip())
cnt = 0
array = [500, 100, 50, 10]

for coin in array:
  cnt += n // coin
  n %= coin

print(cnt)

**정당성 분석: 가지고 있는 동전이 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올 수 없기 때문
