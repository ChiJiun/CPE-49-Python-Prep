"""UVA 10170 - The Hotel with Infinite Rooms
Core: find the smallest n whose arithmetic-series sum reaches D.
Time: O(log answer) per case.
"""

def enough(n, s, d):
    return n * (n + 1) // 2 - (s - 1) * s // 2 >= d

def solve():
    while True:
        try:
            s, d = map(int, input().split())
        except EOFError:
            break

        left = s
        right = max(s, d)

        while left < right:
            mid = (left + right) // 2

            if enough(mid, s, d):
                right = mid
            else:
                left = mid + 1

        print(left)

if __name__ == "__main__":
    solve()
