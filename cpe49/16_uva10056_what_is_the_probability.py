"""UVA 10056
Core: evaluate a finite repeating geometric process.
Time: O(1) per case.
"""
import sys

def solve():
    a = sys.stdin.buffer.read().split()
    if not a:
        return
    t = int(a[0])
    k = 1
    out = []
    for _ in range(t):
        n = int(a[k])
        p = float(a[k + 1])
        i = int(a[k + 2])
        k += 3
        if p == 0.0:
            x = 0.0
        else:
            q = 1.0 - p
            x = p * q ** (i - 1) / (1.0 - q ** n)
        out.append(f"{x:.4f}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
