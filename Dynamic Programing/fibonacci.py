"""
피보나치 수열 - 점화식으로 표현 가능: (n번째 수) = (n-1번째 수) + (n-2번째 수)
"""

def fibo(x):
  if x == 1 or x == 2:
    return 1
  return fibo(x-1) + fibo(x-2)
    
# 단순 재귀함수로 피보나치 수열 구현 시 중복되는 부분이 존재하여 시간 복잡도가 지수 스케일이 됨
# 최적 부분 구조와 중복되는 부분 문제 조건을 만족하므로 다이나믹 프로그래밍 사용 가능
# 탑다운 방식의 다이나믹 프로그래밍

d = [0] * 100

def fibo(x):
  if x == 1 or x == 2:
    return 1
  if d[x] != 0:
    return d[x]
  d[x] = d[x-1] + d[x-2]
  return d[x]
