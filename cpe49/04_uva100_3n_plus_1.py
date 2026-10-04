"""UVA 100 - The 3n + 1 Problem
Core: evaluate maximum Collatz cycle length on each inclusive interval.
Time: proportional to visited Collatz states, with memoization.
"""
import sys

memo = {1: 1}

def cycle_len(n):
    x = n
    path = []
    while x not in memo:
        path.append(x)
        x = x // 2 if x % 2 == 0 else 3 * x + 1
    length = memo[x]
    for v in reversed(path):
        length += 1
        memo[v] = length
    return memo[n]

def solve():
    out = []
    for line in sys.stdin.buffer:
        if not line.strip():
            continue
        i, j = map(int, line.split())
        lo, hi = min(i, j), max(i, j)
        best = max(cycle_len(n) for n in range(lo, hi + 1))
        out.append(f"{i} {j} {best}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
