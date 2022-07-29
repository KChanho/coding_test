"""
일직선으로 이어진 식량창고를 습격해서 식량을 빼앗으려 한다.
이때, 서로 인접한 식량창고를 습격하면 정찰병에게 들킨다.
얻을 수 있는 식량의 최댓값을 구하는 프로그램을 작성하세요.
"""

n = int(input())
array = list(map(int, input().split()))

# i번째 식량창고까지의 최적의 해를 구하는 식으로 분리하여 다이나믹 프로그래밍 적용

d = [0] * (n + 1)
