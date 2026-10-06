"""UVA 272 - TEX Quotes
Core: replace alternating double quotes with TeX opening/closing quotes.
Time: O(total characters).
"""

def solve():
    opening = True

    while True:
        try:
            line = input()
        except EOFError:
            break

        result = ""

        for ch in line:
            if ch == '"':
                if opening:
                    result += "``"
                else:
                    result += "''"
                opening = not opening
            else:
                result += ch

        print(result)

if __name__ == "__main__":
    solve()
