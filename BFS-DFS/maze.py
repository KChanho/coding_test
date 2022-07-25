"""
N x M 크기의 직사각형 형태의 미로에 갇혔을 때, 미로의 괴물들을 피해 탈출해야 한다고 가정하자.
초기 위치는 (1, 1)이며 미로의 출구는 (N, M)에 존재하고 한 번에 한 칸씩 이동할 수 있다.
괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다.
탈출하기 위해 움직여야 하는 최소 칸의 개수를 구해라.
"""

# BFS를 사용하여 풀이 - 최단거리

from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
  
def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if graph[nx][ny] == 0:
        continue
      # 해당 노드를 처음 방문하는 경우에만 최단 거리 
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  # 목적지까지의 최단 거리 반환
  return graph[n-1][m-1]
  
print(bfs(0, 0))
