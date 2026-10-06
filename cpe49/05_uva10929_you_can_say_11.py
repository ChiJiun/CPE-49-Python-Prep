"""UVA 10929 - You can say 11
Core: a decimal integer is divisible by 11 iff its alternating digit sum is.
Time: O(number of digits).
"""

def solve():
    while True:
        s = input()

        if s == "0":
            break

        diff = 0

        for i, ch in enumerate(s):
            if i % 2 == 0:
                diff += int(ch)
            else:
                diff -= int(ch)

        if diff % 11 == 0:
            print(f"{s} is a multiple of 11.")
        else:
            print(f"{s} is not a multiple of 11.")

if __name__ == "__main__":
    solve()
