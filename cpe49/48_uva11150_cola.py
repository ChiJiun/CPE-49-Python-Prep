"""UVA 11150 - Cola
Core: with the allowed one-bottle loan, total drinks are n + floor(n/2).
Time: O(1) per input.
"""
import sys

def solve():
    nums = [int(x) for x in sys.stdin.buffer.read().split()]
    sys.stdout.write("\n".join(str(n + n // 2) for n in nums))

if __name__ == "__main__":
    solve()
