"""UVA 11332 - Summing Digits
Core: repeatedly sum decimal digits until one digit remains.
Time: O(number of processed digits).
"""
import sys

def solve():
    out = []
    for token in sys.stdin.buffer.read().split():
        n = int(token)
        if n == 0:
            break
        while n >= 10:
            n = sum(map(int, str(n)))
        out.append(str(n))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
