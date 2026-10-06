"""UVA 10193 - All You Need Is Love!
Core: binary values share a nontrivial common divisor iff gcd > 1.
Time: O(log min(a,b)).
"""
from math import gcd

def solve():
    t = int(input())

    for case in range(1, t + 1):
        a = int(input(), 2)
        b = int(input(), 2)

        if gcd(a, b) > 1:
            print(f"Pair #{case}: All you need is love!")
        else:
            print(f"Pair #{case}: Love is not all you need!")

if __name__ == "__main__":
    solve()
