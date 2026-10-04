"""UVA 10038 - Jolly Jumpers
Core: adjacent absolute differences must be exactly 1..n-1.
Time: O(n).
"""
import sys

def solve():
    out = []
    for line in sys.stdin.buffer:
        nums = list(map(int, line.split()))
        if not nums:
            continue
        n = nums[0]
        a = nums[1:1+n]
        diffs = {abs(a[i] - a[i-1]) for i in range(1, len(a))}
        out.append("Jolly" if diffs == set(range(1, n)) else "Not jolly")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
