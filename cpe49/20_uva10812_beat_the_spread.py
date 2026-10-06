"""UVA 10812 - Beat the Spread!
Core: solve x+y=s and x-y=d, requiring nonnegative integer results.
Time: O(1) per case.
"""

def solve():
    t = int(input())

    for _ in range(t):
        s, d = map(int, input().split())

        if s < d or (s + d) % 2 == 1:
            print("impossible")
        else:
            high = (s + d) // 2
            low = (s - d) // 2
            print(high, low)

if __name__ == "__main__":
    solve()
