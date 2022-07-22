# 유클리드 호제법: 최대공약수를 구하는 대표적인 알고리즘
# 두 자연수 A, B (A > B)에 대하여 A를 B로 나눈 나머지를 R이라고 한다.
# 이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같다.

def gcd(a, b):
  if a % b == 0:
    return b
  else:
    return gcd(b, a % b)
