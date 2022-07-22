# DFS/BFS
- 대표적인 그래프 탐색 알고리즘

### 스택 자료구조
- 먼저 들어온 데이터가 나중에 나가는 형식(선입후출)의 자료구조
- 파이썬에서 리스트의 append(), pop() 메소드를 활용하여 구현 가능

```python
stack = []
stack.append(1)
stack.append(2)
stack.pop() # 2

print(stack)  # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력
```

### 큐 자료구조
- 먼저 들어온 데이터가 먼저 나가는 형식(선입선출)의 자료구조
- deque 라이브러리를 활용하여 사용 가능 (리스트 자료형으로 구현하는 것보다 효율적)

```python
from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.popleft() # 2

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse()
print(queue)  # 나중에 들어온 원소부터 출력
```

### 재귀 함수
- 자기 자신을 다시 호출하는 함수
- 무한 루프를 방지하기 위해, 종료 조건을 반드시 명시해야 함
- 모든 재귀 함수는 반복문을 이용하여 동일한 기능을 구현할 수 있음
- 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓이기 때문에, 스택을 사용해야 할 때 스택 라이브러리 대신 재귀 함수를 이용할 수 있음 ex) DFS ..

```python
def recursive_function(i):
  # 종료 조건
  if i == 100:
    return
  print(i, "번째 재귀함수에서", i+1, "번째 재귀함수를 호출합니다.")
  recursive_function(i+1)
  print(i, "번째 재귀함수를 종료합니다.")
  
recursive_function(1)
```

## DFS (Depth-First Search)
- 깊이 우선 탐색, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
- 스택 자료구조(혹은 재귀함수)를 이용하며, 구체적인 동작 과정은 다음과 같다.
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.

```python
def dfs(graph, v, visited):
  # 현재 노드를 방문 처리
  visited[v] = True
  print(v, end=' ')
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)
      
# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7],
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

dfs(graph, 1, visited)
```

## BFS (Breadth-First Search)
- 너비 우선 탐색, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
- 큐 자료구조를 이용하며, 구체적인 동작 과정은 다음과 같다.
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리한다.
3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.
