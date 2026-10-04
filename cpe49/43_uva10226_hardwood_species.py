"""UVA 10226 - Hardwood Species
Core: count each species name and output sorted percentages to four decimals.
Time: O(n log k) per case.
"""
import sys
from collections import Counter

def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    t = int(lines[0].strip())
    idx = 1
    blocks = []
    for _ in range(t):
        while idx < len(lines) and lines[idx] == "":
            idx += 1
        cnt = Counter()
        total = 0
        while idx < len(lines) and lines[idx] != "":
            cnt[lines[idx]] += 1
            total += 1
            idx += 1
        block = []
        if total:
            for name in sorted(cnt):
                block.append(f"{name} {cnt[name] * 100.0 / total:.4f}")
        blocks.append("\n".join(block))
    sys.stdout.write("\n\n".join(blocks))

if __name__ == "__main__":
    solve()
