"""UVA 10050 - Hartals
Core: mark strike days and ignore Friday/Saturday weekends.
Time: O(N * P) in direct simulation.
"""
import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    p = 1
    out = []
    for _ in range(t):
        n = data[p]
        parties = data[p + 1]
        p += 2
        periods = data[p:p+parties]
        p += parties
        lost = set()
        for h in periods:
            for day in range(h, n + 1, h):
                if day % 7 not in (6, 0):
                    lost.add(day)
        out.append(str(len(lost)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
