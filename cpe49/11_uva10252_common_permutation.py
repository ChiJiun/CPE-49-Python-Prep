"""UVA 10252 - Common Permutation
Core: multiset intersection of each pair of input lines.
Time: O(L log L) for output sorting.
"""
import sys
from collections import Counter

def solve():
    lines = sys.stdin.read().splitlines()
    out = []
    for i in range(0, len(lines) - 1, 2):
        a = Counter(lines[i])
        b = Counter(lines[i + 1])
        common = a & b
        out.append("".join(ch * common[ch] for ch in sorted(common)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
