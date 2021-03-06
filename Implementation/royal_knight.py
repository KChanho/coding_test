"""
8 x 8 좌표 평면에 나이트가 하나 서 있다.
나이트는 다음의 2가지 경우로 이동할 수 있다.
1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
나이트의 위치가 주어졌을 때, 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하라.
이때 행 위치는 1부터 8으로, 열 위치는 a부터 h로 표현한다.
"""

import sys

data = input()
move = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
x = int(data[1])
y = int(ord(data[0])) - int(ord('a')) + 1 #문자를 아스키코드로 변환하는 함수 ord()

result = 0
for m in move:
  nx = x + m[0]
  ny = y + m[1]
  if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
    result += 1

print(result)

#시뮬레이션, 완전 탐색 유형
