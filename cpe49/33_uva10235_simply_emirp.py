"""UVA 10235 - Simply Emirp
Core: primality test n and its decimal reversal.
Time: O(sqrt n) per primality check.
"""
from math import isqrt

def is_prime(n):
    if n < 2:
        return False

    if n % 2 == 0:
        return n == 2

    limit = isqrt(n)
    divisor = 3

    while divisor <= limit:
        if n % divisor == 0:
            return False

        divisor += 2

    return True

def solve():
    while True:
        try:
            n = int(input())
        except EOFError:
            break

        reversed_n = int(str(n)[::-1])

        if not is_prime(n):
            print(f"{n} is not prime.")
        elif reversed_n != n and is_prime(reversed_n):
            print(f"{n} is emirp.")
        else:
            print(f"{n} is prime.")

if __name__ == "__main__":
    solve()
