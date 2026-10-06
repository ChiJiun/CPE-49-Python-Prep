"""UVA 10783 - Odd Sum
Core: sum odd integers in each inclusive interval.
Time: O(length of interval), small constraints.
"""

def solve():
    t = int(input())

    for case in range(1, t + 1):
        a = int(input())
        b = int(input())

        if a > b:
            a, b = b, a

        total = 0

        for n in range(a, b + 1):
            if n % 2 == 1:
                total += n

        print(f"Case {case}: {total}")

if __name__ == "__main__":
    solve()
