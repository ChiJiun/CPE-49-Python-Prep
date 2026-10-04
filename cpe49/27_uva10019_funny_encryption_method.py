"""UVA 10019 - Funny Encryption Method
Core: count 1-bits in decimal n and in the value formed by reading its decimal digits as hex.
Time: O(number of digits).
"""
import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    out = []
    for n in data[1:1+t]:
        b1 = bin(n).count("1")
        b2 = bin(int(str(n), 16)).count("1")
        out.append(f"{b1} {b2}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
