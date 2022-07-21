"""
한 마을에 모험가가 N명 있고, 각각의 모험가는 각자 공포도를 가진다
공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 한다면 
N이 주어졌을 때, 구성할 수 있는 모험가 그룹 수의 최댓값을 구하는 프로그램을 작성하라
"""

import sys

n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split()))
array.sort()

result = 0
cnt = 0
for x in array:
  cnt += 1
  if cnt >= x:
    result += 1
    cnt = 0

print(result)
  
#정당성 분석: 공포도를 오름차순으로 확인하여 '현재 그룹에 포함된 모험가의 수'가 '현재 확인하고 있는 공포도' 보다 크거나 같다면 그룹으로 설정
