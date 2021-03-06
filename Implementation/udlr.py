"""
여행가 A가 N x N 크기의 정사각형 공간 위에 서 있다.
가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N, N)이다.
A는 상하좌우로 이동할 수 있으며 시작 좌표는 항상 (1, 1)이다.
A의 이동 계획서에는 L, R, U, D 중 하나의 문자가 띄어쓰기로 구분되어 반복적으로 적혀있다.
이때, N x N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다.
"""

import sys

n = int(input())
data = input().split()

direction = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
x, y = 1, 1

for d in data:
  for i in range(len(direction)):
    if d == direction[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  x, y = nx, ny

print(x, y)

#시뮬레이션 유형
#
