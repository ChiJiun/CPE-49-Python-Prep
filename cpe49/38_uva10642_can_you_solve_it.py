"""UVA 10642 - Can You Solve It?
Core: map (x,y) to its index on diagonal traversal, then subtract indices.
Time: O(1) per case.
"""
import sys

def pos(x, y):
    s = x + y
    return s * (s + 1) // 2 + x

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    p = 1
    out = []
    for case in range(1, t + 1):
        x1, y1, x2, y2 = data[p:p+4]
        p += 4
        out.append(f"Case {case}: {pos(x2, y2) - pos(x1, y1)}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
