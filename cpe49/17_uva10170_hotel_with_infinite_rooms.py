"""UVA 10170 - The Hotel with Infinite Rooms
Core: find the smallest n whose arithmetic-series sum reaches D.
Time: O(log answer) per case.
"""
import sys

def enough(n, s, d):
    return n * (n + 1) // 2 - (s - 1) * s // 2 >= d

def solve():
    out = []
    for line in sys.stdin.buffer:
        if not line.strip():
            continue
        s, d = map(int, line.split())
        lo, hi = s, max(s, d)
        while lo < hi:
            mid = (lo + hi) // 2
            if enough(mid, s, d):
                hi = mid
            else:
                lo = mid + 1
        out.append(str(lo))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
