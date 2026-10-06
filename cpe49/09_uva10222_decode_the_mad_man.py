"""UVA 10222 - Decode the Mad man
Core: lowercase each non-space input character and map it two keyboard positions left.
Time: O(total characters).
"""

KEYBOARD = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"

def decode(line):
    result = ""

    for ch in line:
        if ch == " ":
            result += " "
            continue

        low = ch.lower()
        index = KEYBOARD.find(low)

        if index >= 2:
            result += KEYBOARD[index - 2]
        else:
            result += ch

    return result

def solve():
    while True:
        try:
            line = input()
        except EOFError:
            break

        print(decode(line))

if __name__ == "__main__":
    solve()
