"""
N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다.
이때, 이 수열에서 x가 등장하는 횟수를 계산하라.
값이 x인 원소가 하나도 없다면 -1을 출력하라.
단, 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 시간 초과 판정을 받음. -> 이진 탐색
"""

import bisect from bisect_left, bisect_right

n, x = map(int, input().split())
array = list(map(int, input().split()))

result = bisect_right(array, x) - bisect_left(array, x)

if result == 0:
  print(-1)
else:
  print(result)
