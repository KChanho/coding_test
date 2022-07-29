"""
피보나치 수열 - 점화식으로 표현 가능: (n번째 수) = (n-1번째 수) + (n-2번째 수)
"""

def fibo(x):
  if x == 1 or x == 2:
    return 1
  return fibo(x-1) + fibo(x-2)
    
