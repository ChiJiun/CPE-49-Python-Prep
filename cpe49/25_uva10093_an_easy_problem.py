"""UVA 10093 - An Easy Problem!
Core: try bases from max_digit+1 to 62; divisibility by base-1 uses digit sum.
Time: O(62 * length).
"""
import sys

def value(ch):
    if "0" <= ch <= "9":
        return ord(ch) - ord("0")
    if "A" <= ch <= "Z":
        return ord(ch) - ord("A") + 10
    if "a" <= ch <= "z":
        return ord(ch) - ord("a") + 36
    return None

def solve():
    out = []
    for line in sys.stdin:
        digits = [value(ch) for ch in line.strip()]
        digits = [d for d in digits if d is not None]
        if not digits:
            out.append("2")
            continue
        start = max(2, max(digits) + 1)
        total = sum(digits)
        answer = None
        for base in range(start, 63):
            if total % (base - 1) == 0:
                answer = base
                break
        out.append(str(answer) if answer is not None else "such number is impossible!")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
