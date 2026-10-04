"""UVA 10908 - Largest Square
Core: expand odd squares around each query while all cells equal the center.
Time: O(min(M,N)^2) worst case per query.
"""
import sys

def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    t = int(lines[0])
    idx = 1
    out = []
    for _ in range(t):
        m, n, q = map(int, lines[idx].split())
        idx += 1
        grid = lines[idx:idx+m]
        idx += m
        out.append(f"{m} {n} {q}")
        for _ in range(q):
            r, c = map(int, lines[idx].split())
            idx += 1
            ch = grid[r][c]
            radius = 0
            while True:
                nr = radius + 1
                if r - nr < 0 or r + nr >= m or c - nr < 0 or c + nr >= n:
                    break
                ok = True
                for i in range(r - nr, r + nr + 1):
                    if grid[i][c - nr] != ch or grid[i][c + nr] != ch:
                        ok = False
                        break
                if ok:
                    for j in range(c - nr, c + nr + 1):
                        if grid[r - nr][j] != ch or grid[r + nr][j] != ch:
                            ok = False
                            break
                if not ok:
                    break
                radius = nr
            out.append(str(radius * 2 + 1))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
