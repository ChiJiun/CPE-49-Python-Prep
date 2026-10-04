"""UVA 12019 - Doom's Day Algorithm
Core: query weekdays for dates in year 2011.
Time: O(1) per case.
"""
import sys
from datetime import date

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    out = []
    p = 1
    for _ in range(t):
        m, d = data[p], data[p + 1]
        p += 2
        out.append(date(2011, m, d).strftime("%A"))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
