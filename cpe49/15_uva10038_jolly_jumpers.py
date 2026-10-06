"""UVA 10038 - Jolly Jumpers
Core: adjacent absolute differences must be exactly 1..n-1.
Time: O(n).
"""

def solve():
    while True:
        try:
            data = list(map(int, input().split()))
        except EOFError:
            break

        if len(data) == 0:
            continue

        n = data[0]
        arr = data[1:1+n]
        differences = set()

        for i in range(1, n):
            differences.add(abs(arr[i] - arr[i - 1]))

        if differences == set(range(1, n)):
            print("Jolly")
        else:
            print("Not jolly")

if __name__ == "__main__":
    solve()
