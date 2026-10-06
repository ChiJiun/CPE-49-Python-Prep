"""UVA 11150 - Cola
Core: with the allowed one-bottle loan, total drinks are n + floor(n/2).
Time: O(1) per case.
"""

def solve():
    while True:
        try:
            n = int(input())
        except EOFError:
            break

        print(n + n // 2)

if __name__ == "__main__":
    solve()
