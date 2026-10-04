"""UVA 490 - Rotating Sentences
Core: output columns left-to-right while reading original rows bottom-to-top.
Time: O(rows * max_width).
"""
import sys

def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    width = max(map(len, lines))
    out = []
    for c in range(width):
        row = []
        for line in reversed(lines):
            row.append(line[c] if c < len(line) else " ")
        out.append("".join(row))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
