"""UVA 299 - Train Swapping
Core: the minimum adjacent swaps equals the inversion count.
Time: O(n^2), sufficient for the small train length.
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
        inv = 0
        for i in range(n):
            for j in range(i + 1, n):
                if a[i] > a[j]:
                    inv += 1
        out.append(f"Optimal train swapping takes {inv} swaps.")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
