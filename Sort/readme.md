# 정렬 알고리즘
- 데이터를 특정한 기준에 따라 순서대로 나열하는 것
- 일반적으로 문제 상황에 따라서 적절한 정렬 알고리즘이 공식처럼 사용됨

### 선택 정렬
- 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복
- N번 가장 작은 원소를 찾아 위치를 바꿔야 되므로 시간 복잡도는 O(N^2)

```python
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
  min_index = i
  for j in range(i+1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[i], array[min_index] =  array[min_index], array[i]
  
print(array)
```

### 삽입 정렬
- 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입 (최소 수행 시 맨 앞 데이터 하나가 정렬 되어있다고 가정)
- 선택 정렬보다 구현 난이도가 높지만, 일반적으로 더 효율적으로 동작
- 삽입 정렬의 시간 복잡도는 O(N^2)이지만, 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작 (최선의 경우 O(N))

```python
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
  for j in range(i, 0, -1):
    if array[j] < array[j-1]:
      array[j], array[j-1] = array[j-1], array[j]
    else:
      break

print(array)
```

### 퀵 정렬
- 기준 데이터를 설정하고, 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법 (큰 데이터는 왼쪽에서부터, 작은 데이터는 오른쪽에서부터 선택 / 선택된 데이터들의 위치가 엇갈리는 경우 피벗과 작은 데이터의 위치를 바꿈)
- 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나
- 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘
- 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(Pivot)로 설정
- 피벗을 기준으로 데이터 묶음을 나누는 작업을 분할(Divide)라고 함
- 피벗을 기준으로 배열을 분할해가며 재귀적으로 수행
- 이상적인 경우 분할이 배열을 절반으로 나눈다면, 시간복잡도는 O(NlogN) (N은 데이터 개수, logN은 분할 횟수)
- 평균적으로 O(NlogN)의 시간 복잡도를 가지고, 최악의 경우 O(N^2)의 시간 복잡도를 가짐 - 첫 번째 원소를 피벗으로 삼으면 이미 정렬된 상태일 때
- 표준 라이브러리는 O(NlogN)을 보장

```python
# 일반적인 퀵 정렬
array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
  if start >= end:
    return
  pivot = start # 피벗은 첫 번째 원소
  left = start + 1
  right = end
  while(left <= right):
    # 피벗보다 큰 데이터를 찾을 때까지 반복
    while(left <= end and array[left] <= array[pivot]):
      left += 1
    # 피벗보다 작은 데이터를 찾을 때까지 반복
    while(rigth > start and array[right] >= array[pivot]):
      right -= 1
    if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
      array[right], array[pivot] = array[pivot], array[right]
    else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
      array[left], array[right] = array[right], array[left]
  quick_sort(array, start, right-1)
  quick_sort(array, right+1, end)

quick_sort(array, 0, len(array) - 1)
print(array)
```

```python
# 파이썬의 장점을 살린 퀵 정렬 구현
array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array):
  if len(array) <= 1:
    return array
  pivot = array[0]
  tail = array[1:]
  
  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]
  
  # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
```
