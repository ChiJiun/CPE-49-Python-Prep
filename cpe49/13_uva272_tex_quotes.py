"""UVA 272 - TEX Quotes
Core: replace alternating double quotes with TeX opening/closing quotes.
Time: O(total characters).
"""
import sys

def solve():
    text = sys.stdin.read()
    opening = True
    out = []
    for ch in text:
        if ch == '"':
            out.append("``" if opening else "''")
            opening = not opening
        else:
            out.append(ch)
    sys.stdout.write("".join(out))

if __name__ == "__main__":
    solve()
