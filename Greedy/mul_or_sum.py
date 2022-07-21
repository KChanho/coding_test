"""
각 자리가 숫자(0~9)로만 이루어진 문자열 S가 주어졌을 때,
왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요
모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정
"""

import sys

str = sys.stdin.readline().rstrip()
result = int(str[0])

for i in range(1, len(str)):
  num = int(data[i])
  if num <= 1 or result <= 1:
    result += num
  else:
    result *= num

print(result)

#정당성 분석: 두 수가 모두 2 이상인 경우에는 곱하고 하나라도 1 이하이면 더하기
#시간복잡도 분석: O(n)
