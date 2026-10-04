"""UVA 10409 - Die Game
Core: simulate the six face values while rolling in four directions.
Time: O(number of commands).
"""
import sys

def solve():
    lines = sys.stdin.read().splitlines()
    idx = 0
    out = []
    while idx < len(lines):
        if not lines[idx].strip():
            idx += 1
            continue
        n = int(lines[idx])
        idx += 1
        if n == 0:
            break
        top, north, east, south, west, bottom = 1, 2, 4, 5, 3, 6
        for _ in range(n):
            cmd = lines[idx].strip()
            idx += 1
            if cmd == "north":
                top, north, south, bottom = south, top, bottom, north
            elif cmd == "south":
                top, north, south, bottom = north, bottom, top, south
            elif cmd == "east":
                top, east, west, bottom = west, top, bottom, east
            elif cmd == "west":
                top, east, west, bottom = east, bottom, top, west
        out.append(str(top))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
