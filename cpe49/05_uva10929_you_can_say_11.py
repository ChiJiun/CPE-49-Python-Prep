"""UVA 10929 - You can say 11
Core: a decimal integer is divisible by 11 iff its alternating digit sum is.
Time: O(number of digits).
"""
import sys

def solve():
    out = []
    for token in sys.stdin.buffer.read().split():
        s = token.decode()
        if s == "0":
            break
        diff = sum(int(ch) if i % 2 == 0 else -int(ch) for i, ch in enumerate(s))
        if diff % 11 == 0:
            out.append(f"{s} is a multiple of 11.")
        else:
            out.append(f"{s} is not a multiple of 11.")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
