def find_max_min(arr):
    return max(arr), min(arr)

arr = list(map(int, input("Enter elements separated by spaces: ").split()))
maximum, minimum = find_max_min(arr)
print(f"Maximum: {maximum}, Minimum: {minimum}")
