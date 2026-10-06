"""UVA 10062 - Tell me the frequencies!
Core: sort present ASCII codes by frequency ascending, then ASCII descending.
Time: O(L + k log k) per line.
"""
from collections import Counter

def solve():
    first_case = True

    while True:
        try:
            line = input()
        except EOFError:
            break

        if not first_case:
            print()

        first_case = False
        count = Counter()

        for ch in line:
            count[ord(ch)] += 1

        items = list(count.items())
        items.sort(key=lambda x: (x[1], -x[0]))

        for code, frequency in items:
            print(code, frequency)

if __name__ == "__main__":
    solve()
