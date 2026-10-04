"""UVA 10235 - Simply Emirp
Core: primality test n and its decimal reversal.
Time: O(sqrt n) per primality check.
"""
import sys
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    limit = isqrt(n)
    d = 3
    while d <= limit:
        if n % d == 0:
            return False
        d += 2
    return True

def solve():
    out = []
    for token in sys.stdin.buffer.read().split():
        n = int(token)
        r = int(str(n)[::-1])
        if not is_prime(n):
            out.append(f"{n} is not prime.")
        elif r != n and is_prime(r):
            out.append(f"{n} is emirp.")
        else:
            out.append(f"{n} is prime.")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
