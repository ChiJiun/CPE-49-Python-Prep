"""UVA 11321 - Sort! Sort!! and Sort!!!
Core: sort by C/C++ remainder, odd before even, odd descending, even ascending.
Time: O(n log n) per case.
"""

def c_remainder(n, m):
    if n >= 0:
        return n % m

    return -((-n) % m)

def sort_key(n, m):
    remainder = c_remainder(n, m)
    odd = n % 2 != 0

    if odd:
        return (remainder, 0, -n)

    return (remainder, 1, n)

def read_n_ints(n):
    values = []

    while len(values) < n:
        values.extend(list(map(int, input().split())))

    return values

def solve():
    while True:
        n, m = map(int, input().split())
        print(n, m)

        if n == 0 and m == 0:
            break

        values = read_n_ints(n)
        values.sort(key=lambda x: sort_key(x, m))

        for value in values:
            print(value)

if __name__ == "__main__":
    solve()
