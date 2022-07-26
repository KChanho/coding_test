"""
떡 절단기에 높이(H)를 지정하면 줄 지어진 떡을 한번에 절단한다. (높이가 H 이상인 떡만 잘리고, 그보다 낮은 떡은 잘리지 않음)
손님은 절단기에 의해 잘려진 떡을 가져간다.
손님이 왔을 때 요청한 총 길이가 M이라면, 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.
"""

from bisect import bisect_right

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

# 절단기 높이 h가 커질수록 손님에게 주어지는 떡의 총 길이는 줄어들고, 높이 h가 작아질수록 손님에게 주어지는 떡의 총 길이는 늘어남
result = 0
while (strat <= end):
  total = 0
  mid = (start + end) // 2
  for x in array:
    if x > mid:
      total += x - mid
  # 떡의 양이 부족한 경우 더 많이 자르기 (h 값 줄이기)
  if total < m:
    end = mid - 1
  # 떡의 양이 충분한 경우 덜 자르기 (h 값 늘리기)
  else:
    result = mid
    start = mid + 1
    
print(result)
 
# 절단기의 높이는 0부터 10억까지의 정수 중 하나 -> 탐색 범위가 매우 크므로 효과적인 탐색 방법인 이진 탐색 활용
