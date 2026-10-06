"""UVA 12019 - Doom's Day Algorithm
Core: query weekdays for dates in year 2011.
Time: O(1) per case.
"""
from datetime import date

def solve():
    t = int(input())

    for _ in range(t):
        month, day = map(int, input().split())
        print(date(2011, month, day).strftime("%A"))

if __name__ == "__main__":
    solve()
