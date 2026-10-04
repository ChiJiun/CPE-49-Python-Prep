"""UVA 10922 - 2 the 9s
Core: test divisibility by 9 using digit sums and count reductions to 9.
Time: O(number of processed digits).
"""
import sys

def solve():
    out = []
    for token in sys.stdin.buffer.read().split():
        s = token.decode()
        if s == "0":
            break
        total = sum(map(int, s))
        if total % 9 != 0:
            out.append(f"{s} is not a multiple of 9.")
            continue
        degree = 1
        while total > 9:
            total = sum(map(int, str(total)))
            degree += 1
        out.append(f"{s} is a multiple of 9 and has 9-degree {degree}.")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
