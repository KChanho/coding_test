def factorial_iterative(n):
  if n <= 1:
    return 1
  # 반복문 없이 점화식으로 작성
  return n * factorial_iterative(n-1)

factorial_iterative(5)
