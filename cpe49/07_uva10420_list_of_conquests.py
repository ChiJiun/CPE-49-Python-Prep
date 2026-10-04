"""UVA 10420 - List of Conquests
Core: count the first token (country) of each line, then sort by country.
Time: O(n log k).
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
        if line.strip():
            cnt[line.split()[0]] += 1
    sys.stdout.write("\n".join(f"{country} {cnt[country]}" for country in sorted(cnt)))

if __name__ == "__main__":
    solve()
