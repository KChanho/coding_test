# 이진 탐색 알고리즘
### 순차 탐색: 
리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
### 이진 탐색: 
정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
- 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정
- 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 연산 획수는 log(2)N에 비례
- 이진 탐색은 탐색 범위를 절반씩 줄이며, 시간 복잡도 O(logN) 보장

```python
def binary_search(array, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary_search(array, target, start, mid-1)
  else:
    return binary_search(array, target, mid+1, end)
  
n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print(result+1)
```
