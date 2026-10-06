"""UVA 10057 - A mid-summer night's dream
Core: optimal integers are between the two middle values of the sorted data.
Time: O(n log n) per case.
"""

def read_n_ints(n):
    values = []

    while len(values) < n:
        values.extend(list(map(int, input().split())))

    return values

def solve():
    while True:
        try:
            n = int(input())
        except EOFError:
            break

        values = read_n_ints(n)
        values.sort()

        low = values[(n - 1) // 2]
        high = values[n // 2]

        count = 0

        for value in values:
            if low <= value <= high:
                count += 1

        choices = high - low + 1

        print(low, count, choices)

if __name__ == "__main__":
    solve()
