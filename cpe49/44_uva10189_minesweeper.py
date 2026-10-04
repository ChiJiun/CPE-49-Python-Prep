"""UVA 10189 - Minesweeper
Core: for each non-mine cell count mines in its eight neighbors.
Time: O(n*m).
"""
import sys

DIR8 = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def solve():
    lines = sys.stdin.read().splitlines()
    idx = 0
    field = 1
    blocks = []
    while idx < len(lines):
        if not lines[idx].strip():
            idx += 1
            continue
        n, m = map(int, lines[idx].split())
        idx += 1
        if n == 0 and m == 0:
            break
        grid = lines[idx:idx+n]
        idx += n
        out = [f"Field #{field}:"]
        for r in range(n):
            row = []
            for c in range(m):
                if grid[r][c] == "*":
                    row.append("*")
                    continue
                count = 0
                for dr, dc in DIR8:
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < n and 0 <= cc < m and grid[rr][cc] == "*":
                        count += 1
                row.append(str(count))
            out.append("".join(row))
        blocks.append("\n".join(out))
        field += 1
    sys.stdout.write("\n\n".join(blocks))

if __name__ == "__main__":
    solve()
