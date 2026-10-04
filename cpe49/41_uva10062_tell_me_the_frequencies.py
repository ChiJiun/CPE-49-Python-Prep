"""UVA 10062 - Tell me the frequencies!
Core: sort present ASCII codes by frequency ascending, then ASCII descending.
Time: O(L + k log k) per line.
"""
import sys
from collections import Counter

def solve():
    lines = sys.stdin.read().splitlines()
    blocks = []
    for line in lines:
        cnt = Counter(ord(ch) for ch in line)
        items = sorted(cnt.items(), key=lambda p: (p[1], -p[0]))
        blocks.append("\n".join(f"{code} {freq}" for code, freq in items))
    sys.stdout.write("\n\n".join(blocks))

if __name__ == "__main__":
    solve()
