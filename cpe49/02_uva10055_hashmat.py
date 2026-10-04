"""UVA 10055 - Hashmat the Brave Warrior
Core: print the absolute difference for every pair until EOF.
Time: O(1) per line.
"""
import sys

def solve():
    out = []
    for line in sys.stdin.buffer:
        if not line.strip():
            continue
        a, b = map(int, line.split())
        out.append(str(abs(a - b)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
