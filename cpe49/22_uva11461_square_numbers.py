"""UVA 11461 - Square Numbers
Core: count perfect squares in [a,b] using integer square roots.
Time: O(1) per case.
"""
from math import isqrt

def solve():
    while True:
        a, b = map(int, input().split())

        if a == 0 and b == 0:
            break

        answer = isqrt(b) - isqrt(a - 1)
        print(answer)

if __name__ == "__main__":
    solve()
