"""UVA 10252 - Common Permutation
Core: multiset intersection of each pair of input lines.
Time: O(L log L) for output sorting.
"""
from collections import Counter

def solve():
    while True:
        try:
            a = input()
            b = input()
        except EOFError:
            break

        count_a = Counter(a)
        count_b = Counter(b)
        common = count_a & count_b

        result = ""

        for ch in sorted(common):
            result += ch * common[ch]

        print(result)

if __name__ == "__main__":
    solve()
