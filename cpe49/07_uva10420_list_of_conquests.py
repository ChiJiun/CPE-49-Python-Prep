"""UVA 10420 - List of Conquests
Core: count the first token (country) of each line, then sort by country.
Time: O(n log k).
"""
from collections import Counter

def solve():
    n = int(input())
    count = Counter()

    for _ in range(n):
        line = input()
        country = line.split()[0]
        count[country] += 1

    for country in sorted(count):
        print(country, count[country])

if __name__ == "__main__":
    solve()
