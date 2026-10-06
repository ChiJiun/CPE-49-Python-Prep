"""UVA 10922 - 2 the 9s
Core: test divisibility by 9 using digit sums and count reductions to 9.
Time: O(number of processed digits).
"""

def solve():
    while True:
        s = input()

        if s == "0":
            break

        total = sum(list(map(int, s)))

        if total % 9 != 0:
            print(f"{s} is not a multiple of 9.")
            continue

        degree = 1

        while total > 9:
            total = sum(list(map(int, str(total))))
            degree += 1

        print(f"{s} is a multiple of 9 and has 9-degree {degree}.")

if __name__ == "__main__":
    solve()
