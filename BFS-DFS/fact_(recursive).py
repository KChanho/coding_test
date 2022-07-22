def factorial_iterative(n):
  if n <= 1:
    return 1
  return n * factorial_iterative(n-1)

factorial_iterative(5)
