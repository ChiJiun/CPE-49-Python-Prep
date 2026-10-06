"""UVA 11349 - Symmetric Matrix
Core: all values must be nonnegative and the flattened matrix palindromic.
Time: O(n^2).
"""

def solve():
    t = int(input())

    for case in range(1, t + 1):
        line = input()
        n = int(line.split("=")[1])

        values = []

        while len(values) < n * n:
            values.extend(list(map(int, input().split())))

        ok = True

        for value in values:
            if value < 0:
                ok = False
                break

        if ok and values != values[::-1]:
            ok = False

        if ok:
            print(f"Test #{case}: Symmetric.")
        else:
            print(f"Test #{case}: Non-symmetric.")

if __name__ == "__main__":
    solve()
