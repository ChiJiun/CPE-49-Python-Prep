"""UVA 11063 - B2-Sequence
Core: positive strictly increasing terms and all pair sums (i<=j) unique.
Time: O(n^2).
"""
import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    case = 1
    out = []
    while p < len(data):
        n = data[p]
        p += 1
        a = data[p:p+n]
        p += n
        ok = len(a) == n and all(x > 0 for x in a) and all(a[i] < a[i+1] for i in range(n-1))
        seen = set()
        if ok:
            for i in range(n):
                for j in range(i, n):
                    s = a[i] + a[j]
                    if s in seen:
                        ok = False
                        break
                    seen.add(s)
                if not ok:
                    break
        label = "a B2-Sequence." if ok else "not a B2-Sequence."
        out.append(f"Case #{case}: It is {label}")
        out.append("")
        case += 1
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
