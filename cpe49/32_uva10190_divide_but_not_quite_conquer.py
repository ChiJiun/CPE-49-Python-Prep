"""UVA 10190 - Divide, But Not Quite Conquer!
Core: repeatedly divide by m only when exactly divisible until reaching 1.
Time: O(log_m n).
"""

def solve():
    while True:
        try:
            n, m = map(int, input().split())
        except EOFError:
            break

        if m < 2 or n < 2:
            print("Boring!")
            continue

        sequence = [n]
        x = n
        ok = True

        while x != 1:
            if x % m != 0:
                ok = False
                break

            x //= m
            sequence.append(x)

        if ok:
            print(*sequence)
        else:
            print("Boring!")

if __name__ == "__main__":
    solve()
