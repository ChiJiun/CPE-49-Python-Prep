"""UVA 100 - The 3n + 1 Problem
Core: evaluate maximum Collatz cycle length on each inclusive interval.
Time: proportional to visited Collatz states, with memoization.
"""

memo = {1: 1}

def cycle_len(n):
    x = n
    path = []

    while x not in memo:
        path.append(x)
        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1

    length = memo[x]

    for value in reversed(path):
        length += 1
        memo[value] = length

    return memo[n]

def solve():
    while True:
        try:
            i, j = map(int, input().split())
        except EOFError:
            break

        lo = min(i, j)
        hi = max(i, j)
        best = 0

        for n in range(lo, hi + 1):
            best = max(best, cycle_len(n))

        print(i, j, best)

if __name__ == "__main__":
    solve()
