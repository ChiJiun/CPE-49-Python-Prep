"""UVA 10035 - Primary Arithmetic
Core: simulate decimal addition and count carry operations.
Time: O(number of digits).
"""
import sys

def solve():
    out = []
    for line in sys.stdin.buffer:
        if not line.strip():
            continue
        a, b = map(int, line.split())
        if a == 0 and b == 0:
            break
        carry = 0
        count = 0
        while a or b:
            if a % 10 + b % 10 + carry >= 10:
                carry = 1
                count += 1
            else:
                carry = 0
            a //= 10
            b //= 10
        if count == 0:
            out.append("No carry operation.")
        elif count == 1:
            out.append("1 carry operation.")
        else:
            out.append(f"{count} carry operations.")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
