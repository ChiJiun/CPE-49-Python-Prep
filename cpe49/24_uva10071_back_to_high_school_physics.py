"""UVA 10071 - Back to High School Physics
Core: displacement after the symmetric interval is 2*v*t.
Time: O(1) per line.
"""
import sys

def solve():
    out = []
    for line in sys.stdin.buffer:
        if line.strip():
            v, t = map(int, line.split())
            out.append(str(2 * v * t))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
