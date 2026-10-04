"""UVA 11349 - Symmetric Matrix
Core: all values must be nonnegative and the flattened matrix palindromic.
Time: O(n^2).
"""
import sys

def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    t = int(lines[0].strip())
    idx = 1
    out = []
    for case in range(1, t + 1):
        while idx < len(lines) and not lines[idx].strip():
            idx += 1
        n = int(lines[idx].split("=")[1].strip())
        idx += 1
        vals = []
        while len(vals) < n * n and idx < len(lines):
            vals.extend(map(int, lines[idx].split()))
            idx += 1
        ok = all(x >= 0 for x in vals) and vals == vals[::-1]
        label = "Symmetric." if ok else "Non-symmetric."
        out.append(f"Test #{case}: {label}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
