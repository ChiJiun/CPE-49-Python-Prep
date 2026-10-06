"""UVA 11332 - Summing Digits
Core: repeatedly sum decimal digits until one digit remains.
Time: O(number of processed digits).
"""

def solve():
    while True:
        n = int(input())

        if n == 0:
            break

        while n >= 10:
            digits = list(map(int, str(n)))
            n = sum(digits)

        print(n)

if __name__ == "__main__":
    solve()
