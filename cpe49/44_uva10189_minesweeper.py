"""UVA 10189 - Minesweeper
Core: for each non-mine cell count mines in its eight neighbors.
Time: O(n*m).
"""

DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),            (0, 1),
    (1, -1),  (1, 0),   (1, 1),
]

def solve():
    field = 1

    while True:
        n, m = map(int, input().split())

        if n == 0 and m == 0:
            break

        grid = []

        for _ in range(n):
            grid.append(input())

        if field > 1:
            print()

        print(f"Field #{field}:")

        for r in range(n):
            result = ""

            for c in range(m):
                if grid[r][c] == "*":
                    result += "*"
                    continue

                count = 0

                for dr, dc in DIRECTIONS:
                    rr = r + dr
                    cc = c + dc

                    if 0 <= rr < n and 0 <= cc < m:
                        if grid[rr][cc] == "*":
                            count += 1

                result += str(count)

            print(result)

        field += 1

if __name__ == "__main__":
    solve()
