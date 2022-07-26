"""
두 배열 A와 B는 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수이다.
최대 K 번의 바꿔치기 연산을 통해 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이 목표다.
바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 뜻한다.
N, K, 그리고 배열 A와 B의 정보가 주어졌을 때, 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하시오.
"""

# 바꿔치기 수행 시, A의 최솟값과 B의 최댓값을 교환해야함

n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(k):
  # A의 원소가 B의 원소보다 작은 경우
  if A[i] < B[i]:
    A[i], B[i] = B[i], A[i]
  else:
    break
  
print(sum(A))
