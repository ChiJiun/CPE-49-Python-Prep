"""UVA 10071 - Back to High School Physics
Core: displacement after the symmetric interval is 2*v*t.
Time: O(1) per case.
"""

def solve():
    while True:
        try:
            v, t = map(int, input().split())
        except EOFError:
            break

        print(2 * v * t)

if __name__ == "__main__":
    solve()
