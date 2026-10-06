"""UVA 299 - Train Swapping
Core: the minimum adjacent swaps equals the inversion count.
Time: O(n^2), sufficient for the small train length.
"""

def read_n_ints(n):
    values = []

    while len(values) < n:
        values.extend(list(map(int, input().split())))

    return values

def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())
        train = read_n_ints(n)
        inversions = 0

        for i in range(n):
            for j in range(i + 1, n):
                if train[i] > train[j]:
                    inversions += 1

        print(f"Optimal train swapping takes {inversions} swaps.")

if __name__ == "__main__":
    solve()
