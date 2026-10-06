"""UVA 10226 - Hardwood Species
Core: count each species name and output sorted percentages to four decimals.
Time: O(n log k) per case.
"""
from collections import Counter

def solve():
    t = int(input())
    lines = []

    while True:
        try:
            lines.append(input())
        except EOFError:
            break

    groups = []
    current = []

    for line in lines:
        if line == "":
            if len(current) > 0:
                groups.append(current)
                current = []
        else:
            current.append(line)

    if len(current) > 0:
        groups.append(current)

    for case in range(t):
        if case > 0:
            print()

        trees = groups[case]
        count = Counter(trees)
        total = len(trees)

        for name in sorted(count):
            percentage = count[name] * 100.0 / total
            print(f"{name} {percentage:.4f}")

if __name__ == "__main__":
    solve()
