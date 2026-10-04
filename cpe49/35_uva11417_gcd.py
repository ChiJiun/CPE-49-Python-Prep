"""UVA 11417 - GCD
Core: precompute G(n)=sum gcd(i,j) for 1<=i<j<=n incrementally.
Time: O(maxN^2 log maxN) preprocessing.
"""
import sys
from math import gcd

def solve():
    nums = [int(x) for x in sys.stdin.buffer.read().split()]
    queries = []
    for n in nums:
        if n == 0:
            break
        queries.append(n)
    if not queries:
        return
    m = max(queries)
    g = [0] * (m + 1)
    for n in range(2, m + 1):
        add = 0
        for i in range(1, n):
            add += gcd(i, n)
        g[n] = g[n - 1] + add
    sys.stdout.write("\n".join(str(g[n]) for n in queries))

if __name__ == "__main__":
    solve()
