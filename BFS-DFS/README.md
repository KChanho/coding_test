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
