"""UVA 11461 - Square Numbers
Core: count perfect squares in [a,b] using integer square roots.
Time: O(1) per case.
"""
import sys
from math import isqrt

def solve():
    out = []
    for line in sys.stdin.buffer:
        if not line.strip():
            continue
        a, b = map(int, line.split())
        if a == 0 and b == 0:
            break
        out.append(str(isqrt(b) - isqrt(a - 1)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
