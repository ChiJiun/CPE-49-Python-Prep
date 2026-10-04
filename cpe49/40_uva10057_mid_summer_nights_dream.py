"""UVA 10057 - A mid-summer night's dream
Core: optimal integers are between the two middle values of the sorted data.
Time: O(n log n) per case.
"""
import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    out = []
    while p < len(data):
        n = data[p]
        p += 1
        a = data[p:p+n]
        p += n
        a.sort()
        lo = a[(n - 1) // 2]
        hi = a[n // 2]
        count = sum(1 for x in a if lo <= x <= hi)
        choices = hi - lo + 1
        out.append(f"{lo} {count} {choices}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
