"""UVA 10783 - Odd Sum
Core: sum odd integers in each inclusive interval.
Time: O(length of interval), small constraints.
"""
import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    p = 1
    out = []
    for case in range(1, t + 1):
        a, b = data[p], data[p + 1]
        p += 2
        if a > b:
            a, b = b, a
        first = a if a % 2 else a + 1
        ans = sum(range(first, b + 1, 2))
        out.append(f"Case {case}: {ans}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
