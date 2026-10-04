"""UVA 10931
Core: convert an integer to binary and count set bits.
Time: O(log n).
"""
import sys

def solve():
    out = []
    for token in sys.stdin.buffer.read().split():
        n = int(token)
        if n == 0:
            break
        b = bin(n)[2:]
        c = b.count("1")
        out.append(f"The parity of {b} is {c} (mod 2).")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
