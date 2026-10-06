"""UVA 10050 - Hartals
Core: mark strike days and ignore Friday/Saturday weekends.
Time: O(N * P) in direct simulation.
"""

def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())
        p = int(input())
        periods = []

        for _ in range(p):
            periods.append(int(input()))

        lost = set()

        for h in periods:
            for day in range(h, n + 1, h):
                if day % 7 != 6 and day % 7 != 0:
                    lost.add(day)

        print(len(lost))

if __name__ == "__main__":
    solve()
