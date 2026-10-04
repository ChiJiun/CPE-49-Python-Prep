"""UVA 10812 - Beat the Spread!
Core: solve x+y=s and x-y=d, requiring nonnegative integer results.
Time: O(1) per case.
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
        s, d = data[p], data[p + 1]
        p += 2
        if s < d or (s + d) % 2:
            out.append("impossible")
        else:
            out.append(f"{(s + d)//2} {(s - d)//2}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
