"""UVA 10008 - What's Cryptanalysis?
Core: case-insensitive alphabet frequency; sort by count desc then letter asc.
Time: O(total characters).
"""
import sys
from collections import Counter

def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    n = int(lines[0])
    cnt = Counter()
    for line in lines[1:n+1]:
        for ch in line.upper():
            if "A" <= ch <= "Z":
                cnt[ch] += 1
    items = sorted(cnt.items(), key=lambda p: (-p[1], p[0]))
    sys.stdout.write("\n".join(f"{ch} {c}" for ch, c in items))

if __name__ == "__main__":
    solve()
