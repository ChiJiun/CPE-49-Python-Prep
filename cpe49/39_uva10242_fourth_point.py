"""UVA 10242 - Fourth Point!!
Core: identify the duplicated endpoint; missing parallelogram vertex = a+b-duplicate.
Time: O(1) per case.
"""
import sys

def solve():
    out = []
    for line in sys.stdin:
        if not line.strip():
            continue
        v = list(map(float, line.split()))
        p1 = (v[0], v[1])
        p2 = (v[2], v[3])
        p3 = (v[4], v[5])
        p4 = (v[6], v[7])
        if p1 == p3:
            dup, a, b = p1, p2, p4
        elif p1 == p4:
            dup, a, b = p1, p2, p3
        elif p2 == p3:
            dup, a, b = p2, p1, p4
        else:
            dup, a, b = p2, p1, p3
        x = a[0] + b[0] - dup[0]
        y = a[1] + b[1] - dup[1]
        out.append(f"{x:.3f} {y:.3f}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
