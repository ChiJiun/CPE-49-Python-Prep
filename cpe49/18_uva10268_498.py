"""UVA 10268 - 498'
Core: evaluate the derivative of a polynomial at x using Horner's rule.
Time: O(degree).
"""
import sys

def solve():
    lines = sys.stdin.read().splitlines()
    out = []
    i = 0
    while i + 1 < len(lines):
        if not lines[i].strip():
            i += 1
            continue
        x = int(lines[i].strip())
        coeffs = list(map(int, lines[i + 1].split()))
        i += 2
        n = len(coeffs) - 1
        ans = 0
        for j, c in enumerate(coeffs[:-1]):
            ans = ans * x + c * (n - j)
        out.append(str(ans))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
