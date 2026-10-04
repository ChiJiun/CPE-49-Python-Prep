"""UVA 10041 - Vito's Family
Core: the median minimizes the sum of absolute distances.
Time: O(n log n) per case.
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
        p += 1
        a = data[p:p+n]
        p += n
        a.sort()
        m = a[n // 2]
        out.append(str(sum(abs(x - m) for x in a)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
