"""
어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택해서 수행
1. N에서 1을 뺍니다.
2. N을 K로 나눕니다.  *N이 K로 나누어 떨어질 때만 선택 가능
N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하라
"""

import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
cnt = 0

while True: #단계별로 모두 진행하지 않고, 간단히 정리할 수 있는 것은 한번에 진행
  target = (n // k) * k
  cnt += n - target
  n = target
  if n < k:
    break
  cnt += 1
  n //= k

cnt += n-1
print(cnt)

#정당성 분석: k가 2 이상일 때, k로 나누는 것이 1을 빼는 것보다 빠르게 수를 줄일 수 있으므로 그리디로 최적의 해를 찾을 수 있다 
