"""UVA 10008 - What's Cryptanalysis?
Core: case-insensitive alphabet frequency; sort by count desc then letter asc.
Time: O(total characters).
"""
from collections import Counter

def solve():
    n = int(input())
    count = Counter()

    for _ in range(n):
        line = input().upper()

        for ch in line:
            if "A" <= ch <= "Z":
                count[ch] += 1

    items = list(count.items())
    items.sort(key=lambda x: (-x[1], x[0]))

    for ch, freq in items:
        print(ch, freq)

if __name__ == "__main__":
    solve()
