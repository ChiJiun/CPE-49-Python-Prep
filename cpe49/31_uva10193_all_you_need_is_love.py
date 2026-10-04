"""UVA 10193 - All You Need Is Love!
Core: binary values share a nontrivial common divisor iff gcd > 1.
Time: O(log min(a,b)).
"""
import sys
from math import gcd

def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    t = int(lines[0])
    out = []
    idx = 1
    for case in range(1, t + 1):
        a = int(lines[idx].strip(), 2)
        b = int(lines[idx + 1].strip(), 2)
        idx += 2
        if gcd(a, b) > 1:
            out.append(f"Pair #{case}: All you need is love!")
        else:
            out.append(f"Pair #{case}: Love is not all you need!")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
