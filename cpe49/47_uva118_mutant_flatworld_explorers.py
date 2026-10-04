"""UVA 118 - Mutant Flatworld Explorers
Core: simulate robots; remember scented edge positions that suppress repeated falls.
Time: O(total instructions).
"""
import sys

DIRS = "NESW"
MOVE = {"N":(0,1), "E":(1,0), "S":(0,-1), "W":(-1,0)}

def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    max_x, max_y = map(int, lines[0].split())
    idx = 1
    scents = set()
    out = []
    while idx < len(lines):
        if not lines[idx].strip():
            idx += 1
            continue
        x_txt, y_txt, d = lines[idx].split()
        x, y = int(x_txt), int(y_txt)
        idx += 1
        instructions = lines[idx].strip() if idx < len(lines) else ""
        idx += 1
        lost = False
        facing = DIRS.index(d)
        for cmd in instructions:
            if cmd == "L":
                facing = (facing - 1) % 4
            elif cmd == "R":
                facing = (facing + 1) % 4
            else:
                direction = DIRS[facing]
                dx, dy = MOVE[direction]
                nx, ny = x + dx, y + dy
                if 0 <= nx <= max_x and 0 <= ny <= max_y:
                    x, y = nx, ny
                elif (x, y) in scents:
                    continue
                else:
                    scents.add((x, y))
                    lost = True
                    break
        line = f"{x} {y} {DIRS[facing]}"
        if lost:
            line += " LOST"
        out.append(line)
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
