def factorial_dp(n, memo=None):
  """Calculate factorial using top-down approach"""
  if memo is None:
    memo = {}
  
  if n == 0 or n == 1:
      return 1
  if n in memo:
      return memo[n]
  """Store result in memo"""
  memo[n] = n * factorial_dp(n-1, memo)
  return memo[n]

# Use Input
num = int(input("Enter a number : "))

if num < 0:
  print("Please enter a positive number!")
else:
  print(f"{num}! is {factorial_dp(num)}")
