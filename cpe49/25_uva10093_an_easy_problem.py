"""UVA 10093 - An Easy Problem!
Core: try bases from max_digit+1 to 62; divisibility by base-1 uses digit sum.
Time: O(62 * length).
"""

def value(ch):
    if "0" <= ch <= "9":
        return ord(ch) - ord("0")

    if "A" <= ch <= "Z":
        return ord(ch) - ord("A") + 10

    if "a" <= ch <= "z":
        return ord(ch) - ord("a") + 36

    return None

def solve():
    while True:
        try:
            line = input()
        except EOFError:
            break

        digits = []

        for ch in line:
            digit = value(ch)

            if digit is not None:
                digits.append(digit)

        if len(digits) == 0:
            print(2)
            continue

        start = max(2, max(digits) + 1)
        total = sum(digits)
        answer = None

        for base in range(start, 63):
            if total % (base - 1) == 0:
                answer = base
                break

        if answer is None:
            print("such number is impossible!")
        else:
            print(answer)

if __name__ == "__main__":
    solve()
