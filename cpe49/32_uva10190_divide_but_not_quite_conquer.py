"""UVA 10190 - Divide, But Not Quite Conquer!
Core: repeatedly divide by m only when exactly divisible until reaching 1.
Time: O(log_m n).
"""
import sys

def solve():
    out = []
    for line in sys.stdin.buffer:
        if not line.strip():
            continue
        n, m = map(int, line.split())
        if m < 2 or n < 2:
            out.append("Boring!")
            continue
        seq = [n]
        x = n
        ok = True
        while x != 1:
            if x % m != 0:
                ok = False
                break
            x //= m
            seq.append(x)
        out.append(" ".join(map(str, seq)) if ok else "Boring!")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
