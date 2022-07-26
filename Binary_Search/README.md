# 이진 탐색 알고리즘
### 순차 탐색: 
리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
### 이진 탐색: 
정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
- 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정
- 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 연산 획수는 log(2)N에 비례
- 이진 탐색은 탐색 범위를 절반씩 줄이며, 시간 복잡도 O(logN) 보장

```python
def binary_search(array, target, start, end):
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

### 파이썬 이진 탐색 라이브러리
- bisect_left(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
- bisect_right(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

```python
from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4

print(bisect_left(a, x)
# 2
print(bisect_right(a, x)
# 4
```

### 파라메트릭 서치 (Parametric Search)
- 최적화 문제를 결정 문제('예' 혹은 '아니오')로 바꾸어 해결하는 기법
- 일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 이진 탐색을 이용하여 해
