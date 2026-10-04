"""UVA 10222 - Decode the Mad man
Core: lowercase each non-space input character and map it two keyboard positions left.
Time: O(total characters).
"""
import sys

KEYBOARD = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"

def solve():
    text = sys.stdin.read()
    out = []
    for ch in text:
        low = ch.lower()
        if ch.isspace():
            out.append(ch)
            continue
        i = KEYBOARD.find(low)
        out.append(KEYBOARD[i - 2] if i >= 2 else ch)
    sys.stdout.write("".join(out))

if __name__ == "__main__":
    solve()
