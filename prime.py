def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

n = int(input("Enter a number: "))
print(f"{n} is {'a prime' if is_prime(n) else 'not a prime'} number.")