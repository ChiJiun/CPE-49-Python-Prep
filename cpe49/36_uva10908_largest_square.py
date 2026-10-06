"""UVA 10908 - Largest Square
Core: expand odd squares around each query while all cells equal the center.
Time: O(min(M,N)^2) worst case per query.
"""

def solve():
    t = int(input())

    for _ in range(t):
        m, n, q = map(int, input().split())
        grid = []

        for _ in range(m):
            grid.append(input())

        print(m, n, q)

        for _ in range(q):
            r, c = map(int, input().split())
            target = grid[r][c]
            radius = 0

            while True:
                next_radius = radius + 1

                if r - next_radius < 0:
                    break
                if r + next_radius >= m:
                    break
                if c - next_radius < 0:
                    break
                if c + next_radius >= n:
                    break

                ok = True

                for row in range(r - next_radius, r + next_radius + 1):
                    if grid[row][c - next_radius] != target:
                        ok = False
                        break
                    if grid[row][c + next_radius] != target:
                        ok = False
                        break

                if ok:
                    for col in range(c - next_radius, c + next_radius + 1):
                        if grid[r - next_radius][col] != target:
                            ok = False
                            break
                        if grid[r + next_radius][col] != target:
                            ok = False
                            break

                if not ok:
                    break

                radius = next_radius

            print(radius * 2 + 1)

if __name__ == "__main__":
    solve()
