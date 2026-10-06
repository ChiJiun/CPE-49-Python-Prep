"""UVA 490 - Rotating Sentences
Core: output columns left-to-right while reading original rows bottom-to-top.
Time: O(rows * max_width).
"""

def solve():
    lines = []

    while True:
        try:
            lines.append(input())
        except EOFError:
            break

    if len(lines) == 0:
        return

    width = max(len(line) for line in lines)

    for col in range(width):
        result = ""

        for line in reversed(lines):
            if col < len(line):
                result += line[col]
            else:
                result += " "

        print(result)

if __name__ == "__main__":
    solve()
