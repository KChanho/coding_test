"""
N x M 크기의 얼음 틀에서 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하세요.
"""

# DFS를 사용하여 풀이

n, m = map(int, input().split())
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

# 따로 추가 자료구조 사용 없이 graph만으로 해결, 반복되는 부분 dfs에 넣어 재귀적으로 수행
def dfs(x, y):
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  if graph[x][y] == 0:
    graph[x][y] = 1
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  return False
      
result = 0
for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      result += 1
      
print(result)
