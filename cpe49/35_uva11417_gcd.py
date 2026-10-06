"""UVA 11417 - GCD
Core: precompute G(n)=sum gcd(i,j) for 1<=i<j<=n incrementally.
Time: O(maxN^2 log maxN) preprocessing.
"""
from math import gcd

def solve():
    queries = []

    while True:
        n = int(input())

        if n == 0:
            break

        queries.append(n)

    if len(queries) == 0:
        return

    maximum = max(queries)
    answer = [0] * (maximum + 1)

    for n in range(2, maximum + 1):
        current = 0

        for i in range(1, n):
            current += gcd(i, n)

        answer[n] = answer[n - 1] + current

    for n in queries:
        print(answer[n])

if __name__ == "__main__":
    solve()
